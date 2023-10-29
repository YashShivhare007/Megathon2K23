import { Container, Row, Col } from "react-bootstrap";
import logo from "../assets/img/Logo.png";
import navIcon1 from "../assets/img/nav-icon1.svg";
import navIcon2 from "../assets/img/nav-icon2.svg";
import navIcon3 from "../assets/img/nav-icon3.svg";

export const Footer = () => {
  return (
    <footer className="footer" id ="footer">
      <Container>
          <br/><br/>
          <Row>
            <h1>About Us</h1>
            <br/><br/><br/>
          <h5>We are Innovative tech company specializing in AI and data solutions that mpowers businesses with smart insights and automation and drives growth and efficiency through cutting-edge technology.</h5>
          </Row>
          <br/><br/><br/>
        <Row className="align-items-center">
          <Col size={12} sm={6}>
            <img src={logo} alt="Logo" />
          </Col>
          <Col size={12} sm={6} className="text-center text-sm-end">
            <div className="social-icon">
              <a href="https://in.linkedin.com/company/konnectnxt"><img src={navIcon1} alt="Icon" /></a>
              <a href="https://www.facebook.com/KonnectNxt/"><img src={navIcon2} alt="Icon" /></a>
              <a href="https://www.instagram.com/konnectnxthq/"><img src={navIcon3} alt="Icon" /></a>
            </div>
            <p>Copyright 2022. All Rights Reserved</p>
          </Col>
        </Row>
      </Container>
    </footer>
  )
}
