import { useContext } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Profile = () => {
  const { user, logoutUser } = useContext(AuthContext);
  return (
    <div>
      <Link to="/">Home</Link>
      <span> | </span>
      {user ? (
        <div>
          <p onClick={logoutUser}>Logout</p>
          <p>Hello {user.user_id}</p>
        </div>
      ) : (
        <Link to="/login">Login</Link>
      )}
    </div>
  );
};

export default Profile;
