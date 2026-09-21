import { useState } from "react";
import type { MouseEvent } from "react";

import {
  Avatar,
  Box,
  Chip,
  IconButton,
  Menu,
  MenuItem,
  Typography,
} from "@mui/material";

import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import LogoutIcon from "@mui/icons-material/Logout";

import { useLocation, useNavigate } from "react-router-dom";

import type { CurrentUser } from "../../types/auth";
import { clearTokens } from "../../services/tokenService";


interface HeaderProps {
  currentUser: CurrentUser;
}


const getPageTitle = (pathname: string): string => {
  if (pathname.startsWith("/tickets")) {
    return "Tickets";
  }

  if (pathname.startsWith("/ideas")) {
    return "Ideas";
  }

  if (pathname.startsWith("/team")) {
    return "Team";
  }

  if (pathname.startsWith("/ai")) {
    return "AI Assistant";
  }

  return "Dashboard";
};


const Header = ({ currentUser }: HeaderProps) => {
  const navigate = useNavigate();
  const location = useLocation();

  const [menuAnchor, setMenuAnchor] =
    useState<HTMLElement | null>(null);

  const isMenuOpen = Boolean(menuAnchor);

  const handleOpenMenu = (
    event: MouseEvent<HTMLElement>
  ) => {
    setMenuAnchor(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setMenuAnchor(null);
  };

  const handleLogout = () => {
    clearTokens();
    handleCloseMenu();
    navigate("/login", { replace: true });
  };

  const pageTitle = getPageTitle(location.pathname);

  const avatarLetter =
    currentUser.username.charAt(0).toUpperCase();

  return (
    <Box
      component="header"
      sx={{
        height: 72,
        px: 3,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        borderBottom: "1px solid",
        borderColor: "divider",
        backgroundColor: "background.paper",
      }}
    >
      <Typography
        component="h1"
        variant="h5"
        sx={{
          fontWeight: 600,
        }}
      >
        {pageTitle}
      </Typography>

      <Box
        sx={{
          display: "flex",
          alignItems: "center",
          gap: 1.5,
        }}
      >
        <Chip
          label={currentUser.role}
          size="small"
          variant="outlined"
        />

        <Typography
          variant="body2"
          sx={{
            fontWeight: 500,
          }}
        >
          {currentUser.username}
        </Typography>

        <IconButton
          onClick={handleOpenMenu}
          aria-label="Open user menu"
          aria-controls={
            isMenuOpen
              ? "user-menu"
              : undefined
          }
          aria-haspopup="true"
          aria-expanded={
            isMenuOpen
              ? "true"
              : undefined
          }
        >
          <Avatar
            sx={{
              width: 36,
              height: 36,
              fontSize: "0.9rem",
            }}
          >
            {avatarLetter}
          </Avatar>

          <KeyboardArrowDownIcon
            fontSize="small"
          />
        </IconButton>

        <Menu
          id="user-menu"
          anchorEl={menuAnchor}
          open={isMenuOpen}
          onClose={handleCloseMenu}
          anchorOrigin={{
            vertical: "bottom",
            horizontal: "right",
          }}
          transformOrigin={{
            vertical: "top",
            horizontal: "right",
          }}
        >
          <MenuItem onClick={handleLogout}>
            <LogoutIcon
              fontSize="small"
              sx={{ mr: 1 }}
            />

            Logout
          </MenuItem>
        </Menu>
      </Box>
    </Box>
  );
};

export default Header;