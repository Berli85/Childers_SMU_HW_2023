d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json");
    console.log(data);

    //Select the dropdown
    let dropdown = d3.select("#selDataset");

    for (let i = 0; i < data.names.length; i++){
        let name = data.names[i];
        dropdown.append("option").text(name);
    }

    let person = data.names[0];
    let person_data = data.samples.filter(row => row.id === person)[0];
    console.log(person_data);