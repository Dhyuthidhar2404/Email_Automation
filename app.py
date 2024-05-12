from flask import Flask, request, render_template
import os
import yagmail

app = Flask(__name__)

# Set a secret key for session management and CSRF protection
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Define the upload folder where attachments will be saved
UPLOAD_FOLDER = 'C:\\Users\\S.S.S.Dhyuthidhar\\Videos\\Email_Automation_Python\\attachments'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        try:
            sender_email = request.form['username']
            sender_password = request.form['password']
            recipient_email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']
            
            # Check if attachment file was provided
            if 'attachment' in request.files:
                attachment = request.files['attachment']
                # Save the attachment to the upload folder
                attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], attachment.filename)
                attachment.save(attachment_path)
            else:
                attachment_path = None

            # Send email using yagmail
            yag = yagmail.SMTP(user=sender_email, password=sender_password)
            yag.send(to=recipient_email, subject=subject, contents=message, attachments=attachment_path)

            return 'Email sent successfully'
        except Exception as e:
            return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # Run with HTTPS using a self-signed certificate
