import { useCallback, useEffect, useState } from "react";
import { Navigate, Outlet } from "react-router-dom";
import axios from "axios";

import { getCurrentUser } from "../services/authService";
import {
  clearTokens,
  getAccessToken,
} from "../services/tokenService";
import type {CurrentUser} from "../types/auth.ts";

type AuthStatus =
  | "checking"
  | "authenticated"
  | "unauthenticated"
  | "error";

const ProtectedRoute = () => {
  const [currentUser, setCurrentUser] = useState<CurrentUser | null>(null);
  const [authStatus, setAuthStatus] =
    useState<AuthStatus>("checking");

  const verifyAuthentication = useCallback(async () => {
    const accessToken = getAccessToken();

    if (!accessToken) {
      setAuthStatus("unauthenticated");
      return;
    }

    setAuthStatus("checking");

    try {
      const user = await getCurrentUser();

      setCurrentUser(user);
      setAuthStatus("authenticated");
    } catch (error) {
      if (
        axios.isAxiosError(error) &&
        error.response?.status === 401
      ) {
        clearTokens();
        setAuthStatus("unauthenticated");
        return;
      }

      setAuthStatus("error");
    }
  }, []);

  useEffect(() => {
    void verifyAuthentication();
  }, [verifyAuthentication]);

  if (authStatus === "checking") {
    return <p>Checking authentication...</p>;
  }

  if (authStatus === "unauthenticated") {
    return <Navigate to="/login" replace />;
  }

  if (authStatus === "error") {
    return (
      <div>
        <p>Unable to verify your session.</p>
        <button onClick={verifyAuthentication}>
          Try again
        </button>
      </div>
    );
  }

  return <Outlet context={{ currentUser }} />;
};

export default ProtectedRoute;