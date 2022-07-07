import React from "react";
import { Link } from "react-router-dom";
const Problem = ({ problem }) => {
	// let getTitle = (problem) => {

	// 	let title = problem.body.split('\n')[0]
	// 	if (problem.length > 45) {
	// 		return title.slice(0, 45)
	// 	}
	// 	return title
	// }
	return (
		<Link to={`/problems/${problem.id}`} key={problem.id}>
			<div className='notes-list-item'>
				<h3>{problem.question_name}</h3>
				{/* <p>
					{getContent(note)}
				</p> */}
			</div>
		</Link>
	);
};

export default Problem;
