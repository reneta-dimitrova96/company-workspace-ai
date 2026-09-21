import {BrowserRouter, Route, Routes} from "react-router-dom";

import ProtectedRoute from "./components/ProtectedRoute";
import LoginPage from "./pages/Login/LoginPage.tsx";
import RegisterPage from "./pages/Register/RegisterPage.tsx";
import TicketsPage from "./pages/Tickets/TicketsPage.tsx";
import IdeasPage from "./pages/Ideas/IdeasPage.tsx";
import TeamPage from "./pages/Team/TeamPage.tsx";
import AIAssistantPage from "./pages/AIAssistant/AIAssistantPage.tsx";
import DashboardPage from "./pages/Dashboard/DashboardPage.tsx";
import AppLayout from "./components/layout/AppLayout.tsx";
import './App.css'


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/register" element={<RegisterPage/>}/>
        <Route element={<ProtectedRoute/>}>
          <Route element={<AppLayout/>}>
            <Route path="/dashboard" element={<DashboardPage/>}/>
            <Route path="/tickets" element={<TicketsPage/>}/>
            <Route path="/ideas" element={<IdeasPage/>}/>
            <Route path="/team" element={<TeamPage/>}/>
            <Route path="/ai" element={<AIAssistantPage/>}/>
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
