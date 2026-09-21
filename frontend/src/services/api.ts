import axios, {
  type AxiosError,
  type AxiosRequestConfig,
  type InternalAxiosRequestConfig,
} from "axios";

import type { RefreshResponse } from "../types/auth";
import {
  clearTokens,
  getAccessToken,
  getRefreshToken,
  updateAccessToken,
} from "./tokenService";


const API_BASE_URL = "http://127.0.0.1:8000/api";

const axiosConfig: AxiosRequestConfig = {
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
};


interface RetryableRequestConfig extends InternalAxiosRequestConfig {
  _retry?: boolean;
}


const api = axios.create(axiosConfig);
const refreshClient = axios.create(axiosConfig);


let refreshPromise: Promise<string> | null = null;


const refreshAccessToken = async (): Promise<string> => {
  const refreshToken = getRefreshToken();

  if (!refreshToken) {
    throw new Error("Refresh token is missing.");
  }

  const response = await refreshClient.post<RefreshResponse>(
    "/auth/refresh/",
    {
      refresh: refreshToken,
    }
  );

  updateAccessToken(response.data);

  return response.data.access;
};


api.interceptors.request.use((config) => {
  const accessToken = getAccessToken();

  if (accessToken) {
    config.headers.set(
      "Authorization",
      `Bearer ${accessToken}`
    );
  }

  return config;
});


api.interceptors.response.use(
  (response) => response,

  async (error: AxiosError) => {
    const originalRequest =
      error.config as RetryableRequestConfig | undefined;

    if (
      error.response?.status !== 401 ||
      !originalRequest
    ) {
      return Promise.reject(error);
    }

    const isAuthRequest =
      originalRequest.url?.includes("/auth/login/") ||
      originalRequest.url?.includes("/auth/refresh/");

    if (isAuthRequest || originalRequest._retry) {
      return Promise.reject(error);
    }

    const refreshToken = getRefreshToken();

    if (!refreshToken) {
      clearTokens();
      return Promise.reject(error);
    }

    originalRequest._retry = true;

    try {
      if (!refreshPromise) {
        refreshPromise = refreshAccessToken().finally(() => {
          refreshPromise = null;
        });
      }

      const newAccessToken = await refreshPromise;

      originalRequest.headers.set(
        "Authorization",
        `Bearer ${newAccessToken}`
      );

      return api(originalRequest);
    } catch (refreshError) {
      if (
        axios.isAxiosError(refreshError) &&
        (
          refreshError.response?.status === 400 ||
          refreshError.response?.status === 401
        )
      ) {
        clearTokens();
      }

      return Promise.reject(refreshError);
    }
  }
);


export default api;