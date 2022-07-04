import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";

function App() {
	const [problems, setProblems] = useState(null);
	useEffect(() => {
		// fetch("http://localhost:8000/oj/problems/")
		try {
			const res = fetch("http://localhost:8000/oj/problems/");
			const questionList = res.json();
			console.log(questionList);
			setProblems(questionList);
		} catch (e) {
			console.log(e);
		}
	}, []);
	return <div className='App'>HI dude</div>;
}

export default App;
