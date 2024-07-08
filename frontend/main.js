window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const functionApiUrl = 'https://pb-getresumecounter.azurewebsites.net/api/ResumeCountFunc?code=WYphCB74yamZbjLtATEbDvnSLZJVPqgdajgesvWxs2t2AzFui8ug6w%3D%3D'
const localfunctionApi = 'http://localhost:7071/api/ResumeCountFunc';

const getVisitCount = () => {
    let count = 30;
    fetch(functionApiUrl).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count = response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    })
    return count;
}