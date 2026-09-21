export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access: string;
  refresh: string;
}

export type UserRole = "OWNER" | "ADMIN" | "EMPLOYEE";

export interface CurrentUser {
  id: number;
  username: string;
  email: string;
  role: UserRole;
  company: number | null;
}

export interface RefreshResponse {
  access: string;
}