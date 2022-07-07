import logo from "./logo.svg";
import axios from "axios";
import { useEffect, useState } from "react";
import ProblemsPage from "./components/Problempage";
import Problem from "./components/Problem";
import Problemdetails from "./components/Problemdetails";
import "./App.css";
import { BrowserRouter, Routes, Router, Route } from "react-router-dom";
function App() {
	return (
		<BrowserRouter>
			<Routes>
				{/* sdfsd */}
				<Route path='/' exact element={<ProblemsPage />} />
				<Route path='/problems/:id' element={<Problemdetails />} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;
