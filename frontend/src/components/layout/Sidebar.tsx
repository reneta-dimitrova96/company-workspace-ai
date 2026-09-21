import {
  Box,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import ConfirmationNumberIcon from "@mui/icons-material/ConfirmationNumber";
import LightbulbIcon from "@mui/icons-material/Lightbulb";
import PeopleIcon from "@mui/icons-material/People";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";

import { NavLink, useLocation } from "react-router-dom";

import "./Sidebar.scss";


const menuItems = [
  {
    label: "Dashboard",
    path: "/dashboard",
    icon: <DashboardIcon />,
  },
  {
    label: "Tickets",
    path: "/tickets",
    icon: <ConfirmationNumberIcon />,
  },
  {
    label: "Ideas",
    path: "/ideas",
    icon: <LightbulbIcon />,
  },
  {
    label: "Team",
    path: "/team",
    icon: <PeopleIcon />,
  },
  {
    label: "AI Assistant",
    path: "/ai",
    icon: <AutoAwesomeIcon />,
  },
];


const Sidebar = () => {
  const location = useLocation();

  return (
    <Box
      component="aside"
      sx={{
        width: "240px",
        height: "100vh",
        position: "fixed",
        borderRight: "1px solid",
        borderColor: "divider",
      }}
    >
      <h3 className="sidebar__title">
        Company Workspace AI
      </h3>

      <List
        component="nav"
        aria-label="main navigation"
      >
        {menuItems.map((item) => (
          <ListItemButton
            key={item.path}
            component={NavLink}
            to={item.path}
            selected={location.pathname.startsWith(item.path)}
          >
            <ListItemIcon>
              {item.icon}
            </ListItemIcon>

            <ListItemText
              primary={item.label}
            />
          </ListItemButton>
        ))}
      </List>
    </Box>
  );
};

export default Sidebar;