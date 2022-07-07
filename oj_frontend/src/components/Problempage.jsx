import React, { useState, useEffect } from "react";
import Problem from "./Problem";
import axios from "axios";

const Problempage = () => {
	const [problems, setProblems] = useState([]);

	useEffect(() => {
		// fetch("http://localhost:8000/oj/problems/")
		axios
			.get("http://127.0.0.1:8000/oj/problems/")
			.then((res) => {
				setProblems(res.data);
				// console.log(problems);
			})
			.catch((err) => console.error(err));
		// try {
		// 	const res = fetch("http://localhost:8000/oj/problems/");
		// 	const questionList = res.json();
		// 	console.log(questionList);
		// 	setProblems(questionList);
		// } catch (e) {
		// 	console.log(e);
		// }
	}, []);
	// console.log(problems[1].question_name);

	return (
		<div className='notes'>
			<div className='notes-header'>
				<h2 className='notes-title'>&#9782; Problems</h2>
				{/* <p className='notes-count'>{problems.length}</p> */}
			</div>

			<div className='notes-list'>
				{problems.map((problem, index) => (
					<Problem key={index} problem={problem} />
				))}
			</div>
			{/* <AddButton /> */}
		</div>
	);
};

export default Problempage;
