const axios = require("axios");
const express = require("express");

const app = express ();

async function createTask() {
    const response = await axios({
      url: 'https://api.capsolver.com/createTask',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        "clientKey": "CAI-CA8F5D78B888FEB049BE5444950CAA9F",
        "task": {
          "type": "ReCaptchaV3TaskProxyLess",
          "websiteURL": "http://localhost:3000",
          "websiteKey": "RECAPTCHA_KEY",
          "pageAction": "register",
          "minScore": 0.7
        }
      }
    });
    const data = response.data;
    return data;
  }

async function trackTask(taskId) {
  const response = await axios({
    url: 'https://api.capsolver.com/getTaskResult',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    data: {
      "clientKey": "CAI-CA8F5D78B888FEB049BE5444950CAA9F",
      taskId,
    }
  });
  const data = response.data;
  return data;
}

app.get("/verify/:taskId", async (req, res) => {
    const {taskId} = req.params;
    const result = await trackTask(taskId)
    res.json(result);
})

app.get('/automate', async (req, res) => {
  const solved = await createTask();
  res.json({ solution: solved })
})

app.get('/', (req, res) => {
    res.sendFile(__dirname+'/index.html')
});

app.listen(3000, () => {
  console.log("app is running out");
});