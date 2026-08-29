import { useEffect, useRef , useState } from "react";

import Message from "./components/Message";
import MessageInput from "./components/MessageInput";
import { streamMessage } from "./services/api";


function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  
  async function handleSend() {
    const message = input.trim();

    if (!message || loading) {
      return;
    }


    const userMessage = {
      role: "user",
      content: message,
    };


    const history = messages.map((message) => ({
      role: message.role,
      content: message.content,
    }));


    setMessages((previousMessages) => [
      ...previousMessages,
      userMessage, {
        role : "assistant",
        content : "",
      },
    ]);

    setInput("");
    setLoading(true);


    try {
      await streamMessage(
        message,
        history,
        (chunk) => {
          setMessages((previousMessages) => {
            const updatedMessages = [...previousMessages];

            const lastMessageIndex = updatedMessages.length - 1;

            updatedMessages[lastMessageIndex] = {
              ...updatedMessages[lastMessageIndex],
              content: 
              updatedMessages[lastMessageIndex].content + chunk,
            };
            return updatedMessages;
          });
        }
      );

    }
    catch (error) {
      console.error("Streaming error:", error);
      setMessages((previousMessages) => {
        const updatedMessages = [...previousMessages];

        const lastMessageIndex = updatedMessages.length - 1;

        updatedMessages[lastMessageIndex] = {
          ...updatedMessages[lastMessageIndex],
          content: 
          "Sorry! I could not connect to DurgeshAI."
        };
        return updatedMessages;
      });

    } 
    finally {
      setLoading(false);
    }
  }


  return (
    <div className="app">

      <header className="header">
        <h1>DurgeshAI</h1>
        <p>AI Portfolio Assistant</p>
      </header>


      <main className="chat-container">

        {messages.length === 0 && (
          <section className="welcome">
            <h2>Welcome to DurgeshAI</h2>

            <p>
              Ask me about Durgesh's skills, projects,
              experience, education, or professional background.
            </p>
          </section>
        )}


        <section className="chat-area">

          {messages.map((message, index) => (
            <Message
              key={index}
              role={message.role}
              content={message.content}
            />
          ))}


          {loading && (
            <div className="streaming-indicator">
              AI is responding...
            </div>
          )}

          <div ref={messagesEndRef} />

        </section>


        <section className="input-area">

          <MessageInput
            value={input}
            onChange={setInput}
            onSend={handleSend}
          />

        </section>

      </main>

    </div>
  );
}


export default App;