
function calculateIrrigationTime() {


    const fieldArea = parseFloat(document.getElementById("fieldArea").value);
    const outletDiameter = parseFloat(document.getElementById("outletDiameter").value);
  
    const waterVelocity = 1;
    const waterDepth = 0.1;
  
    const outletRadius = outletDiameter / 2;
    const waterFlowRate = Math.PI * Math.pow(outletRadius, 2) * waterVelocity;
  
    const waterVolume = fieldArea *waterDepth;
    const timeRequired = waterVolume / waterFlowRate;
  
    const hours = Math.floor(timeRequired / 3600);
    const minutes = Math.floor((timeRequired % 3600) / 60);
    const seconds = Math.floor(timeRequired % 60);
  
  
    const resultElement = document.getElementById("result");
    resultElement.textContent = `Time required to irrigate the field: ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
  
  
  
  
  }
  