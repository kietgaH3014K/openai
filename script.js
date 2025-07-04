const OpenAI = require("openai");

const openai = new OpenAI({
  apiKey: "SrlxY18iY2rKmZnQ3dtkHZIzVW9tN4dH", 
  baseURL: "https://api.deepinfra.com/v1/openai" 
});

async function chatWithAI(message) {
  try {
    const response = await openai.chat.completions.create({
      model: "meta-llama/Meta-Llama-3-8B-Instruct", // ✅ model có thật trên DeepInfra
      messages: [{ role: "user", content: message }],
    });

    console.log("AI:", response.choices[0].message.content);
  } catch (error) {
    console.error("Lỗi khi gọi OpenAI API:", error.response?.data || error.message);
  }
}

chatWithAI("Xin chào, bạn là ai?");
