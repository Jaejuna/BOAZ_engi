import './App.css';
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [place, setPlaces] = useState({
    place_name: "",
    address_name: "",
    place_url: "",
  });
  const myName = "name"; // 본인의 이름을 넣어주세요.

  const url = 'http://localhost:8000/place';

  useEffect(() => {
    const getData = async () => {
      try {
        const res = await axios.get(url);
        console.log(res.data);
        setPlaces(res.data);
      } catch (e) {
        console.error(e.message);
      }
    };
    getData();
  }, []);

  return (
    <div className="App">
      <h1>{myName}의 최고 맛집을 소개합니다 😋</h1>
      <a href={place['place_url']}><h2>{place['place_name']}</h2></a>
      <h3>{place['address_name']}</h3>
      <h4>간단한 소개를 적어주세요!</h4>
    </div>
  );
}

export default App;