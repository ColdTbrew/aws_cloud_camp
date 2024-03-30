const axios = require("axios");

async function postData() {
  try {
    const response = await axios.post(
      "https://lnath3u4svkf2jcamufzqtdgde0hanxc.lambda-url.ap-northeast-2.on.aws/",
      {
        name: "이동령",
        ec2: "elastic compute cloud",
        s3: "simple storage service",
      }
    );
    console.log(response?.data);
  } catch (error) {
    console.error(error);
  }
}

postData();