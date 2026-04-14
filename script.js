async function checkPhishing() {
    const url = document.getElementById("urlInput").value;
    const resultBox = document.getElementById("result");

    if (!url) {
        resultBox.style.display = "block";
        resultBox.className = "result-box phishing";
        resultBox.innerText = "URL을 입력하세요.";
        return;
    }

    resultBox.style.display = "block";
    resultBox.className = "result-box";
    resultBox.innerText = "분석 중입니다...";

    try {
        const response = await fetch("https://your-api-url.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        if (data.result.includes("정상")) {
            resultBox.className = "result-box safe";
            resultBox.innerText = "✅ 정상 사이트입니다.";
        } else {
            resultBox.className = "result-box phishing";
            resultBox.innerText = "⚠️ 피싱 사이트로 의심됩니다.";
        }
    } catch (error) {
        resultBox.className = "result-box phishing";
        resultBox.innerText = "서버 연결 오류가 발생했습니다.";
    }
}
