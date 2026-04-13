async function checkPhishing() {
    const url = document.getElementById("urlInput").value;
    const resultText = document.getElementById("result");

    if (!url) {
        resultText.innerText = "URL을 입력하세요.";
        return;
    }

    try {
        const response = await fetch("https://your-api-url.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();
        resultText.innerText = "분석 결과: " + data.result;
    } catch (error) {
        resultText.innerText = "서버 연결 오류가 발생했습니다.";
    }
}
