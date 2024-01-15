import { Routes, Route } from "react-router-dom";
import Header from "./Header";
import Hero from "./Hero";
import Home from "./Home";
import HeroPowerForm from "./HeroPowerForm";
import Power from "./Power";
import PowerEditForm from "./PowerEditForm";

function App() {
  return (
    <div>
      <Header />
      <main>
        <Routes>
          <Route exact path="/hero_powers/new" element={<HeroPowerForm />} />
          <Route exact path="/powers/:id/edit" element={<PowerEditForm />} />
          <Route exact path="/powers/:id" element={<Power />} />
          <Route exact path="/heroes/:id" element={<Hero />} />
          <Route exact path="/" element={<Home />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
