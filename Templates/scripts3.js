document.addEventListener("DOMContentLoaded", function() {
    const calculateBtn = document.getElementById("calculateBtn");
    calculateBtn.addEventListener("click", function() {
        const area = parseFloat(document.getElementById("area").value);
        const biofertilizerCost = parseFloat(document.getElementById("biofertilizerCost").value);
        const biopesticideCost = parseFloat(document.getElementById("biopesticideCost").value);
        const herbicidesCost = parseFloat(document.getElementById("herbicidesCost").value);

        if (!isNaN(area) && !isNaN(biofertilizerCost) && !isNaN(biopesticideCost) && !isNaN(herbicidesCost)) {
            const fuelCost = 700 * area;
            const labourCost = 1000 * area;
            const seedCost = 500 * area;

            const netExpenses = fuelCost + labourCost + seedCost + biopesticideCost + biofertilizerCost + herbicidesCost;
            const netRevenue = 15000 * area;
            const netProfit = netRevenue - netExpenses;

            displayNetProfit(netProfit, fuelCost, labourCost, seedCost, biopesticideCost, biofertilizerCost, herbicidesCost);
          
        } else {
            displayNetProfit("Invalid input");
        }
    });

    function displayNetProfit(netProfit, fuelCost, labourCost, seedCost, biopesticideCost, biofertilizerCost, herbicidesCost) {
        const netProfitElement = document.getElementById("netProfit");
        netProfitElement.innerHTML = `
            <p>Net Profit: Rs. ${netProfit}</p>
            <p>Fuel Cost: ${fuelCost}</p>
            <p>Labour Cost: ${labourCost}</p>
            <p>Seed Cost: ${seedCost}</p>
            <p>Biopesticide Cost: ${biopesticideCost}</p>
            <p>Biofertilizer Cost: ${biofertilizerCost}</p>
            <p>Herbicides Cost: ${herbicidesCost}</p>
        `;
    }
});
