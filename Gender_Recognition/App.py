import cv2
from face_recognition import faceRecognitionPipeline
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        # Set the initial window size (width x height)
        self.root.geometry("800x600")

        # Load a background image
        background_image_path = Path("background.png")
        if background_image_path.exists():
            self.background_image = tk.PhotoImage(file=background_image_path)
            self.background_label = tk.Label(self.root, image=self.background_image)
            self.background_label.place(relwidth=1, relheight=1)

        # Create a frame to contain the widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Load button images
        image_button_image = tk.PhotoImage(file="image_button.png")
        video_button_image = tk.PhotoImage(file="video_button.png")
        webcam_button_image = tk.PhotoImage(file="webcam_button.png")

        # Create attractive buttons for image and video processing
        self.image_button = tk.Button(
            self.frame,
            text="Process Image",
            image=image_button_image,
            compound=tk.TOP,  # Place image above text
            command=self.process_image,
        )
        self.image_button.grid(row=0, column=0, pady=10, padx=10)

        self.video_button = tk.Button(
            self.frame,
            text="Process Video",
            image=video_button_image,
            compound=tk.TOP,  # Place image above text
            command=self.process_video,
        )
        self.video_button.grid(row=1, column=0, pady=10, padx=10)

        self.webcam_button = tk.Button(
            self.frame,
            text="Process Webcam",
            image=webcam_button_image,
            compound=tk.TOP,  # Place image above text
            command=self.process_webcam,
        )
        self.webcam_button.grid(row=2, column=0, pady=10, padx=10)

        # Load a placeholder image for the right side
        self.placeholder_image = tk.PhotoImage(file="app.png")  # Replace with the path to your image
        self.image_label = tk.Label(self.frame, image=self.placeholder_image)
        self.image_label.grid(row=0, column=1, rowspan=3, pady=10, padx=10)

    def process_image(self):
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            pred_img, pred_dict = faceRecognitionPipeline(file_path)
            self.display_result(pred_img, pred_dict)

    def process_video(self):
        file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video files", "*.mp4;*.avi")])
        if file_path:
            cap = cv2.VideoCapture(file_path)
            self.process_video_capture(cap)

    def process_webcam(self):
        cap = cv2.VideoCapture(0)
        self.process_video_capture(cap)

    def process_video_capture(self, cap):
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            pred_img, pred_dict = faceRecognitionPipeline(frame, path=False)

            cv2.imshow('prediction', pred_img)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def display_result(self, pred_img, pred_dict):
        # Display the image using Matplotlib
        img_rgb = cv2.cvtColor(pred_img, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(10, 10))
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.show()

        # Generate report for each face detected
        for i in range(len(pred_dict)):
            obj_gray = pred_dict[i]['roi']
            obj_eig = pred_dict[i]['eig_img'].reshape(100, 100)

            plt.subplot(1, 2, 1)
            plt.imshow(obj_gray, cmap='gray')
            plt.title('Gray Scale Image')
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.imshow(obj_eig, cmap='gray')
            plt.title('Eigen Image')
            plt.axis('off')

            plt.show()

            print('Predicted Gender =', pred_dict[i]['prediction_name'])
            print('Predicted score = {:,.2f} %'.format(pred_dict[i]['score'] * 100))
            print('-' * 100)


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
