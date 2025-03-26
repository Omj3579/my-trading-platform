window.addEventListener("DOMContentLoaded", () => {
    const chart = LightweightCharts.createChart(document.getElementById("chart"), {
        width: 800,
        height: 500,
        layout: {
            background: { color: "#ffffff" },
            textColor: "#000000",
        },
    });

    const candleSeries = chart.addCandlestickSeries();

    fetch("http://127.0.0.1:8000/api/candles/AAPL")
        .then(response => response.json())
        .then(data => {
            console.log("Loaded data:", data);
            candleSeries.setData(data);
        })
        .catch(error => console.error("Error loading candles:", error));
});
