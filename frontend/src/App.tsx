import MainHome from '../components/home/MainHome'
import MainCourse from '../components/course/MainCourse'
import { Routes, Route } from "react-router-dom";

function App() {

  return (
    <div>
      <Routes>
          <Route path="/" element={<MainHome />} />
          <Route path='/courses' element={<MainCourse/>} />
      </Routes>
    </div>
  )
}

export default App
