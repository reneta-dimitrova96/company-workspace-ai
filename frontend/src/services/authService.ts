import api from "./api";
import type {CurrentUser, LoginRequest, LoginResponse} from "../types/auth";

export const login = async (
  credentials: LoginRequest
): Promise<LoginResponse> => {
  const response = await api.post<LoginResponse>(
    "/auth/login/",
    credentials
  );

  return response.data;
};

export const getCurrentUser = async (): Promise<CurrentUser> => {
  const response = await api.get<CurrentUser>("/auth/me/");

  return response.data;
};