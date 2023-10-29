const express = require('express')
const axios = require('axios')
const app = express()
const port = 3000

app.use(express.static('public'))

app.get('/', (req, res) => {})

app.get('/prediction', async (req, res) => {
  const query = req.query

  var data = []

  for (const [key, value] of Object.entries(query)) {
    data.push(parseInt(value))
  }

  const result = await axios.post('http://localhost:5001/', data)

  const string = result.data.result.toString()

  string.replace(/'/g, '')

  clean = JSON.parse(string)

  console.log(clean)

  res.send(`
 <div style="display: flex; justify-content: center; text-align: center; margin-top: 20px;">
        <h3 style="margin-top: 35px">Suggested Profession:</h3>
        <p id="suggestedProfession" style="font-family: 'Helvetica', Arial, sans-serif; font-size: 24px; color: #333; background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
            Undetermined
        </p>
    </div>


<div style="display: flex; justify-content: center;  height: 100vh; margin: 0; background-color: #f0f0f0;">
    <ul style="list-style: none; padding: 0; text-align: left;">
        <li style="margin-bottom: 10px;">
            <div style="background-color: #007BFF; border-radius: 5px; text-align: left; height: 60px; width: calc(100% + 30px); display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: white; padding: 10px 20px; font-family: 'Helvetica', Arial, sans-serif; margin: 0;">Extroversion:</h2>
                <span style="background-color: white; padding: 5px 20px; border-radius: 10px; font-family: 'Helvetica', Arial, sans-serif; color: #007BFF; margin-right: 10px;">${clean[0].extroversion}</span>
            </div>
        </li>
        <li style="margin-bottom: 10px;">
            <div style="background-color: #FFC107; border-radius: 5px; text-align: left; height: 60px; width: calc(100% + 30px); display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: #333; padding: 10px 20px; font-family: 'Helvetica', Arial, sans-serif; margin: 0;">Neurotic:</h2>
                <span style="background-color: white; padding: 5px 20px; border-radius: 10px; font-family: 'Helvetica', Arial, sans-serif; color: #FFC107; margin-right: 10px;">${clean[0].neurotic}</span>
            </div>
        </li>
        <li style="margin-bottom: 10px;">
            <div style="background-color: #28A745; border-radius: 5px; text-align: left; height: 60px; width: calc(100% + 30px); display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: white; padding: 10px 20px; font-family: 'Helvetica', Arial, sans-serif; margin: 0;">Agreeable:</h2>
                <span style="background-color: white; padding: 5px 20px; border-radius: 10px; font-family: 'Helvetica', Arial, sans-serif; color: #28A745; margin-right: 10px;">${clean[0].agreeable}</span>
            </div>
        </li>
        <li style="margin-bottom: 10px;">
            <div style="background-color: #DC3545; border-radius: 5px; text-align: left; height: 60px; width: calc(100% + 30px); display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: white; padding: 10px 20px; font-family: 'Helvetica', Arial, sans-serif; margin: 0;">Conscientious:</h2>
                <span style="background-color: white; padding: 5px 20px; border-radius: 10px; font-family: 'Helvetica', Arial, sans-serif; color: #DC3545; margin-right: 10px;">${clean[0].conscientious}</span>
            </div>
        </li>
        <li style="margin-bottom: 10px;">
            <div style="background-color: #6610F2; border-radius: 5px; text-align: left; height: 60px; width: calc(100% + 30px); display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: white; padding: 10px 20px; font-family: 'Helvetica', Arial, sans-serif; margin: 0;">Open:</h2>
                <span style="background-color: white; padding: 5px 20px; border-radius: 10px; font-family: 'Helvetica', Arial, sans-serif; color: #6610F2; margin-right: 10px;">${clean[0].open}</span>
            </div>
        </li>
        <li style="margin-bottom: 10px;">
            <div style="background-color: #FF5733; border-radius: 5px; text-align: left; height: 60px; width: calc(100% + 30px); display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: white; padding: 10px 20px; font-family: 'Helvetica', Arial, sans-serif; margin: 0;">Cluster:</h2>
                <span style="background-color: white; padding: 5px 20px; border-radius: 10px; font-family: 'Helvetica', Arial, sans-serif; color: #FF5733; margin-right: 10px;">${clean[0].cluster}</span>
            </div>
        </li>
    </ul>

</div>
    <script>
        // Initialize variables for personality traits (replace with actual values)
        const openness = ${clean[0].open};
        const conscientiousness = ${clean[0].conscientious};
        const extroversion = ${clean[0].extroversion};
        const agreeableness = ${clean[0].agreeable};

        // Initialize a variable to store the suggested profession
        let suggested_profession = "Undetermined";

        // Suggest a profession based on the personality traits (simplified example)
        if (openness > 0.6 && conscientiousness > 0.6) {
            suggested_profession = "Researcher or Scientist";
        } else if (extroversion > 0.6 && agreeableness > 0.6) {
            suggested_profession = "Sales or Customer Service";
        } else if (conscientiousness > 0.6) {
            suggested_profession = "Manager or Administrator";
        } else if (agreeableness > 0.6) {
            suggested_profession = "Social Worker or Counselor";
        }

        // Output the suggested profession on the page
        const suggestedProfessionElement = document.getElementById("suggestedProfession");
        suggestedProfessionElement.textContent = suggested_profession;
    </script>

    `)
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
