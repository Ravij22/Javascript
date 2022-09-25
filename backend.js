async function fetchData() {
    const response = await fetch("Stock_List.json")
    const datapoints = await response.json();
    console.log(datapoints); 

}