from plyer import notification

# --- create notification ---
notification.notify(
    
    title="Python Notification 🔔",
    
    message="Hello Chakri! This notification was sent using Python.",
    
    timeout=10
)

print("Notification sent successfully ✅")