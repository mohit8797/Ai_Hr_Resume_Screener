async function callAPI(url) {
    const resume = document.getElementById("resume").value;
    const job = document.getElementById("job").value;

    const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            resume_text: resume,
            job_description: job
        })
    });

    const data = await res.json();
    document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
}

function scoreResume() {
    callAPI("/api/resume/score");
}

function skillGap() {
    callAPI("/api/resume/skill-gap");
}

function interviewQuestions() {
    callAPI("/api/resume/interview-questions");
}