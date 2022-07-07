import { useState, React, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Problemdetails = () => {
	const [problem, setProblem] = useState([]);
	let params = useParams();
	const [code, setCode] = useState("");
	const [output, setOutput] = useState("");
	const [language, setLanguage] = useState("cpp");
	const [jobId, setJobId] = useState(null);
	const [status, setStatus] = useState(null);
	const [jobDetails, setJobDetails] = useState(null);
	const probId = params.id;
	console.log(params.id);
	// console.log(history);
	useEffect(() => {
		// fetch("http://localhost:8000/oj/problems/")
		axios
			.get(`http://127.0.0.1:8000/oj/problems/${probId}`)
			.then((res) => {
				setProblem(res.data);
				console.log(res.data);
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
	const handleSubmit = async () => {
		const payload = {
			language,
			code
		};
		try {
			//   setOutput("");
			//   setStatus(null);
			//   setJobId(null);
			//   setJobDetails(null);
			const { data } = await axios.post(
				`http://127.0.0.1:8000/oj/problems/${probId}`
			);
			//   if (data.jobId) {
			//     setJobId(data.jobId);
			//     setStatus("Submitted.");

			//     // poll here
			//     pollInterval = setInterval(async () => {
			//       const { data: statusRes } = await axios.get(
			//         `http://localhost:5000/status`,
			//         {
			//           params: {
			//             id: data.jobId,
			//           },
			//         }
			//       );
			//       const { success, job, error } = statusRes;
			//       console.log(statusRes);
			//       if (success) {
			//         const { status: jobStatus, output: jobOutput } = job;
			//         setStatus(jobStatus);
			//         setJobDetails(job);
			//         if (jobStatus === "pending") return;
			//         setOutput(jobOutput);
			//         clearInterval(pollInterval);
			//       } else {
			//         console.error(error);
			//         setOutput(error);
			//         setStatus("Bad request");
			//         clearInterval(pollInterval);
			//       }
			//     }, 1000);
			//   } else {
			//     setOutput("Retry again.");
			//   }
		} catch ({ response }) {
			if (response) {
				const errMsg = response.data.err.stderr;
				setOutput(errMsg);
			} else {
				setOutput("Please retry submitting.");
			}
		}
	};
	console.log(problem);
	return (
		<div className='App'>
			<h1>Online Code Compiler</h1>
			<div>
				{/* <label>Language:</label>
				<select
					// value={language}
					onChange={(e) => {
						//   const shouldSwitch = window.confirm(
						// 	"Are you sure you want to change language? WARNING: Your current code will be lost."
						//   );
						//   if (shouldSwitch) {
						// 	setLanguage(e.target.value);
						//   }
					}}>
					<option value='cpp'>C++</option>
					<option value='py'>Python</option>
				</select> */}
			</div>
			<br />
			{/* <div>
				<button
				//   onClick={setDefaultLanguage}
				>
					Set Default
				</button>
			</div> */}

			<br />
			<h3>{problem.question_name}-</h3>
			<h5>Difficulty- {problem.difficulty}</h5>
			<p>{problem.question_description}</p>
			<textarea
				rows='20'
				cols='75'
				value={code}
				onChange={(e) => {
					setCode(e.target.value);
				}}></textarea>
			<br />
			<button
			// onClick={handleSubmit}
			>
				Submit
			</button>
			{/* <p>{status}</p>
	<p>{jobId ? `Job ID: ${jobId}` : ""}</p>
	<p>{renderTimeDetails()}</p>
	<p>{output}</p> */}
		</div>
	);
};

export default Problemdetails;
