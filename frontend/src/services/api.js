const API_BASE_URL = "http://127.0.0.1:8000";


export async function sendMessage(message, history = []) {
  const response = await fetch(`${API_BASE_URL}/api/chat`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      message,
      history,
    }),
  });


  if (!response.ok) {
    throw new Error("Failed to communicate with the backend");
  }


  const data = await response.json();

  return data.response;
}

export async function streamMessage(message, history = [], onChunk) {

  const response = await fetch(`${API_BASE_URL}/api/chat/stream`,
    {
      method: "POST" ,
      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message,
        history,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to communicate with backend");
  }

  if (!response.body) {
    throw new Error("Streaming is not supported by this response")
  }


  const reader = response.body.getReader();
  const decoder =  new  TextDecoder();

  try {
    while(true) {
      const { value, done} = await reader.read();

      if(done) {
        break;
      }

      const chunk = decoder.decode(value, {
        stream: true,
      });

      if(chunk) {
        onChunk(chunk);
      }
    }

    const finalChunk =  decoder.decode();

    if(finalChunk) {
      onChunk(finalChunk);
    }
  }
  finally {
    reader.releaseLock();
  }
  
}