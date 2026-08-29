function Message({ role, content }) {
  const isUser = role === "user";

  return (
    <div className={`message-row ${isUser ? "user-row" : "ai-row"}`}>
      <div className={`message ${isUser ? "user-message" : "ai-message"}`}>
        <div className="message-role">
          {isUser ? "You" : "DurgeshAI"}
        </div>

        <div className="message-content">
          {content}
        </div>
      </div>
    </div>
  );
}

export default Message;