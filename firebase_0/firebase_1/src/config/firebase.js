// Import the functions you need from the SDKs you need
import { getAuth } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAFpp0EGeZY8BV0Xzkquh6u34xJXN7Wr0k",
  authDomain: "my-amazing-project-3d59c.firebaseapp.com",
  projectId: "my-amazing-project-3d59c",
  storageBucket: "my-amazing-project-3d59c.firebasestorage.app",
  messagingSenderId: "1072030425856",
  appId: "1:1072030425856:web:3014b81021d32b28c609e5",
  measurementId: "G-495G7LNEFG"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAnalytics(app);