document.addEventListener("DOMContentLoaded", function() {
    // Set default value for costing
    const costingInput = document.getElementById("costing");
    costingInput.value = 5000;

    // Calculate net profit
    const calculateBtn = document.getElementById("calculateBtn");
    calculateBtn.addEventListener("click", function() {
        const costing = parseFloat(costingInput.value);
        const revenue = parseFloat(document.getElementById("revenue").value);

        if (!isNaN(costing) && !isNaN(revenue)) {
            const netProfit = revenue - costing;
            displayNetProfit(netProfit);
        } else {
            displayNetProfit("Invalid input");
        }
    });

    function displayNetProfit(value) {
        const netProfitElement = document.getElementById("netProfit");
        netProfitElement.textContent = `Net Profit: ${value}`;
    }
});
