import {auth} from "../config/firebase"
import {createUserWithEmailAndPassword} from "firebase/auth"

function Auth() {


    return(
        <div>
            <input placeholder="Email">
            </input>
            <input placeholder="password...">
            </input>




            <button>Sign Up</button> 
        </div>
    )

}

export default Auth;