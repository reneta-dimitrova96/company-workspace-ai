import { Box } from "@mui/material";
import { Outlet, useOutletContext } from "react-router-dom";

import Sidebar from "./Sidebar";
import Header from "./Header";
import type { CurrentUser } from "../../types/auth";

const SIDEBAR_WIDTH = 240;

interface AuthOutletContext {
  currentUser: CurrentUser;
}

const AppLayout = () => {
  const { currentUser } =
    useOutletContext<AuthOutletContext>();

  return (
    <Box sx={{ minHeight: "100vh" }}>
      <Sidebar />

      <Box
        sx={{
          marginLeft: `${SIDEBAR_WIDTH}px`,
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Header currentUser={currentUser} />

        <Box
          component="main"
          sx={{
            flexGrow: 1,
            padding: 3,
          }}
        >
          <Outlet />
        </Box>
      </Box>
    </Box>
  );
};

export default AppLayout;