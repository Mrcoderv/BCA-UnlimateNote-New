
<div align="center">

**A Project Report Submitted in Partial Fulfillment of the Requirements**
**for the Degree of Bachelor's in Computer Application**

---

# NEPSE Pro
## Nepal Stock Exchange Analysis & Portfolio Management

---

| Name | Registration No. | Symbol No. |
|---|---|---|
| Raghav Panthi | 2023-1-53-0370 | 23530222 |
| Shishir Devkota | 2023-1-53-0220 | 23530121 |
| Shuprabha Mainali | 2023-1-53-0221 | 23530122 |

---

**School of Environmental Science and Management**
**Faculty of Science and Technology**
**Pokhara University, Nepal**

**June, 2025**

</div>

---

## TABLE OF CONTENTS

| Section | Title | Page |
|---|---|---|
| | Table of Contents | ii |
| | List of Figures | iii |
| | List of Tables | iv |
| | List of Abbreviations | v |
| **Chapter 1** | **Introduction** | **1** |
| 1.1 | Background | 1 |
| 1.2 | Objectives | 2 |
| 1.3 | Purpose, Scope, and Applicability | 3 |
| 1.3.1 | Purpose | 3 |
| 1.3.2 | Scope | 3 |
| 1.3.3 | Applicability | 4 |
| 1.4 | Achievements | 4 |
| 1.5 | Organization of Report | 5 |
| **Chapter 2** | **Survey of Technologies** | **6** |
| 2.1 | Review of Similar/Relevant Projects | 6 |
| 2.2 | Technologies Used | 7 |
| **Chapter 3** | **Requirements and Analysis** | **9** |
| 3.1 | Problem Definition | 9 |
| 3.2 | Requirements Specification | 10 |
| 3.3 | Planning and Scheduling | 12 |
| 3.4 | Software and Hardware Requirements | 13 |
| 3.5 | Preliminary Product Description | 14 |
| 3.6 | Conceptual Models | 15 |
| **Chapter 4** | **Design** | **20** |
| 4.1 | Introduction | 20 |
| 4.2 | System Design | 20 |
| 4.3 | Database Design | 24 |
| 4.4 | Interface Design | 27 |
| 4.5 | Summary | 29 |
| **Chapter 5** | **Implementation and Testing** | **30** |
| 5.1 | Implementation Approaches | 30 |
| 5.2 | Coding Details and Code Efficiency | 32 |
| 5.2.1 | Code Efficiency | 33 |
| 5.3 | Testing Approach | 36 |
| 5.3.1 | Unit Testing | 36 |
| 5.3.2 | Integrated Testing | 37 |
| 5.3.3 | Beta Testing | 37 |
| 5.4 | Modifications and Improvements | 38 |
| 5.5 | Test Cases | 39 |
| **Chapter 6** | **Results and Discussion** | **41** |
| 6.1 | Test Reports | 41 |
| 6.2 | User Documentation | 42 |
| **Chapter 7** | **Conclusions** | **45** |
| 7.1 | Conclusion | 45 |
| 7.1.1 | Significance of the System | 45 |
| 7.2 | Limitations of the System | 46 |
| 7.3 | Future Scope of the Project | 47 |
| | References | 48 |

---

## LIST OF FIGURES

| Figure No. | Title | Page |
|---|---|---|
| Figure 3.1 | Gantt Chart – Project Timeline | 13 |
| Figure 3.2 | Use Case Diagram of NEPSE Pro | 16 |
| Figure 3.3 | DFD Level 0 – Context Diagram | 17 |
| Figure 3.4 | DFD Level 1 – Main Processes | 18 |
| Figure 4.1 | System Architecture Diagram | 21 |
| Figure 4.2 | ER Diagram of NEPSE Pro | 25 |
| Figure 4.3 | UML Class Diagram of NEPSE Pro | 27 |
| Figure 4.4 | UML Sequence Diagram – User Registration & Email Verification | 28 |
| Figure 4.5 | UML Sequence Diagram – Trade Execution Flow | 29 |
| Figure 4.6 | Dashboard Page Interface | 30 |
| Figure 4.7 | Chart Page Interface | 30 |

---

## LIST OF TABLES

| Table No. | Title | Page |
|---|---|---|
| Table 2.1 | Comparison of Existing NEPSE Platforms | 6 |
| Table 3.1 | Functional Requirements | 10 |
| Table 3.2 | Requirement Prioritization Table | 11 |
| Table 3.3 | Non-Functional Requirements | 12 |
| Table 3.4 | Software Requirements | 13 |
| Table 3.5 | Hardware Requirements | 14 |
| Table 3.6 | Development Cost Estimation | 14 |
| Table 4.1 | API Endpoints – Authentication | 22 |
| Table 4.2 | API Endpoints – NEPSE Market Data | 23 |
| Table 4.3 | API Endpoints – User Management | 23 |
| Table 4.4 | Database Schema – Users Table | 25 |
| Table 4.5 | Database Schema – Portfolio Table | 26 |
| Table 4.6 | Database Schema – Watchlist Table | 26 |
| Table 4.7 | Database Schema – Transactions Table | 26 |
| Table 5.1 | Broker Commission Tier Structure | 33 |
| Table 5.2 | Unit Test Cases | 39 |
| Table 5.3 | Integration Test Cases | 40 |
| Table 6.1 | Test Report Summary | 41 |

---

## LIST OF ABBREVIATIONS

| Abbreviation | Full Form |
|---|---|
| API | Application Programming Interface |
| BCA | Bachelor's in Computer Application |
| CGT | Capital Gains Tax |
| CORS | Cross-Origin Resource Sharing |
| CSS | Cascading Style Sheet |
| DFD | Data Flow Diagram |
| DP | Depository Participant |
| EMA | Exponential Moving Average |
| ER | Entity-Relationship |
| HTML | Hyper Text Markup Language |
| JS | JavaScript |
| JWT | JSON Web Token |
| LTP | Last Traded Price |
| MACD | Moving Average Convergence Divergence |
| NEPSE | Nepal Stock Exchange |
| NPR | Nepalese Rupee |
| OHLC | Open, High, Low, Close |
| OOP | Object-Oriented Programming |
| ORM | Object Relational Mapper |
| OTP | One-Time Password |
| REST | Representational State Transfer |
| RSI | Relative Strength Index |
| SEBON | Securities Board of Nepal |
| SMA | Simple Moving Average |
| SMTP | Simple Mail Transfer Protocol |
| SQL | Structured Query Language |
| SSO | Single Sign-On |
| UI/UX | User Interface / User Experience |
| UML | Unified Modeling Language |
| URL | Uniform Resource Locator |

---

# CHAPTER 1: INTRODUCTION

## 1.1 Background

Nepal Stock Exchange (NEPSE) is the only stock exchange in Nepal where companies list their shares for trading. Every day, thousands of investors buy and sell stocks through NEPSE [1]. Just like stock markets in other countries, NEPSE generates a huge amount of data every single day, including prices, trading volumes, company information, and market trends [13].

However, getting this information in an easy-to-understand way has always been a challenge for regular investors in Nepal [14]. Most people who want to invest in the stock market find it hard to study patterns and make good decisions because the data is either hard to access or presented in a complicated way [15]. In many cases, investors must depend on multiple websites, social media discussions, or unofficial sources to understand market conditions. This often creates confusion and increases the risk of making poor investment decisions. Beginners especially face difficulties in understanding market trends, price fluctuations, and company performance due to the lack of proper visualization tools and simplified analysis systems.

**NEPSE Pro** is the implemented solution to this problem — a full-stack web application that shows NEPSE stock market data in an easy-to-understand visual format. Investors can see interactive candlestick price charts with technical indicators, track their favorite companies through a personal watchlist, and manage their investment portfolio with Nepal-specific brokerage charge calculations, all in one place [6]. The system helps users compare stock performance, monitor daily market activities, and analyze historical trends through interactive charts and graphs. By combining real-time market data, advanced charting, and portfolio simulation into a single platform, NEPSE Pro makes stock analysis faster, easier, and more accessible for ordinary investors in Nepal.

The application is built using React 19 [3] and Express.js [4] as its core technologies, with a SQLite database for persistence. It is deployed publicly with the frontend on Vercel [8] and the backend API on Render, making it accessible to any user with a modern browser and internet connection.

---

## 1.2 Objectives

The main objectives of this project are:

1. **To gather and display NEPSE stock data:** Collect real-time data from the NEPSE system via the `@rumess/nepse-api` library [2] and present it in a clear, visual format including the NEPSE index, market summary, top gainers, top losers, and a full market watch of all traded scrips.

2. **To implement advanced candlestick charting with technical indicators:** Provide interactive charts using the Lightweight Charts library [6] supporting multiple timeframes (1-minute to monthly) and overlayable technical analysis indicators including Simple Moving Average (SMA), Exponential Moving Average (EMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD).

3. **To develop a portfolio tracker:** Let users record stock purchases and sales, and automatically calculate holdings using an average cost basis method, unrealized profit/loss relative to live prices, realized profit/loss from completed trades, and full transaction history.

4. **To implement Nepal-specific charge calculations:** Accurately compute all costs associated with NEPSE transactions — tiered broker commission (as per SEBON regulations), SEBON fee (0.015%), Depository Participant (DP) charge (Rs. 25 per sell), and Capital Gains Tax (7.5% for holdings under one year; 5% for over one year) — so users understand the real cost of each trade.

5. **To build a personal watchlist feature:** Allow users to save companies they are interested in and have live prices automatically updated every 30 seconds, without needing to search every time.

6. **To build a secure user authentication system:** Support email and password registration with OTP-based email verification, Google OAuth 2.0 single sign-on, JWT-based session management, and profile and password management.

7. **To deploy a production-ready application:** Host the complete system publicly so that it is accessible to any Nepali investor from a browser on any device.

---

## 1.3 Purpose, Scope, and Applicability

### 1.3.1 Purpose

The purpose of NEPSE Pro is to make stock market information accessible to everyone in Nepal, whether they are experienced traders or just starting to learn about investing. By presenting complex market data in clean visual charts and graphs, and by combining official NEPSE data with modern personalized features, the application helps ordinary people in Nepal make better, more informed decisions when investing in the stock market [12].

### 1.3.2 Scope

**What the system does:**

- Displays live NEPSE index value, market summary (turnover, market capitalization, traded volume, total transactions), top gainers, and top losers on a real-time dashboard.
- Provides interactive candlestick charts for any NEPSE-listed security across eight timeframes (1m, 5m, 15m, 1h, 4h, 1D, 1W, 1M) with volume histogram, SMA, EMA, RSI, and MACD indicators.
- Allows users to search all NEPSE-listed securities by symbol or company name.
- Provides a full sortable and searchable market watch table for all actively traded scrips.
- Allows registered users to maintain a personal watchlist with live prices refreshed every 30 seconds.
- Allows registered users to simulate buying and selling stocks from a starting virtual cash balance of Rs. 1,00,000, with all Nepal-specific charges automatically calculated.
- Displays current portfolio holdings, average buy price, current value, unrealized P&L, and transaction history.
- Supports user registration with email OTP verification, Google OAuth login, and profile management.
- Works responsively on both desktop computers and mobile phones.
- Stores each user's data securely so they see only their own watchlist, portfolio, and transactions [7].

**What the system does NOT do:**

- This is not a real trading platform — users cannot actually buy or sell stocks through this application.
- This does not connect to bank accounts or payment systems.
- This does not provide financial advice or investment recommendations.
- This does not predict future stock prices.
- This does not support mobile native apps (iOS/Android) — it is a browser-based web application only.

### 1.3.3 Applicability

NEPSE Pro is applicable to:

- **Retail investors** in Nepal who wish to track NEPSE market movements and evaluate trade decisions before placing real orders through their broker.
- **Finance students** studying stock market analysis within the Nepali market context.
- **New investors** wanting to practice trading strategy without financial risk, using the virtual cash balance.
- **Experienced traders** needing a convenient browser-based tool to apply technical analysis to NEPSE-listed securities.

---

## 1.4 Achievements

The following were successfully achieved during the development and deployment of NEPSE Pro:

- **Full-stack application deployed publicly:** Frontend deployed on Vercel (`nepse-pro.vercel.app`) and backend API on Render (`nepse-pro-backend.onrender.com`), accessible 24/7.

- **Real-time NEPSE market data integration:** Integrated the `@rumess/nepse-api` library [2] with a 5-second in-memory cache to deliver live NEPSE index, market summary, securities list, gainers, losers, and turnover data with minimal external API overhead.

- **Professional-grade charting engine:** Built a TradingView-inspired chart component using Lightweight Charts [6] with 8 timeframes, 4 technical indicators (SMA, EMA, RSI, MACD), real-time 5-second chart updates during intraday sessions, configurable indicator parameters, and a drawing tools toolbar.

- **Nepal-compliant transaction charge engine:** Implemented a dedicated charge calculator module correctly applying the SEBON 5-tier broker commission structure, 0.015% SEBON regulatory fee, Rs. 25 fixed DP charge per sell, and CGT at 7.5% (short-term) or 5% (long-term) on realized profit.

- **Dual authentication system:** Implemented both local email registration with 6-digit OTP verification (via Gmail SMTP using Nodemailer) and Google OAuth 2.0 (via Passport.js), with JWT-based session management for all protected routes.

- **FIFO portfolio engine:** Built a `PortfolioService` class that reconstructs current holdings from ordered transaction history using an average cost method, computes realized P&L on each sell, and enforces balance/quantity constraints at trade execution time.

- **Responsive dark-theme UI:** Implemented a fully dark-themed, mobile-responsive interface using Tailwind CSS 4 with CSS custom properties, providing a professional trading platform aesthetic.

- **Bug identified and fixed:** Beta testing revealed that the NEPSE index was displaying the `close` field (previous session snapshot) rather than `currentValue` (live value) from the API response. This was corrected across all three affected components, and the index cache TTL was extended to 60 seconds to reduce unnecessary API calls.

---

## 1.5 Organization of Report

This report is organized as follows:

- **Chapter 1 – Introduction:** Provides background context, project objectives, scope, applicability, key achievements, and report organization.
- **Chapter 2 – Survey of Technologies:** Reviews existing platforms (NEPSE website, Merolagani, ShareSansar, TradingView) and the technologies and frameworks selected for NEPSE Pro.
- **Chapter 3 – Requirements and Analysis:** Defines the problem, specifies functional and non-functional requirements with prioritization, presents the project timeline (Gantt chart), hardware/software requirements, budget, preliminary product description, and conceptual models (Use Case Diagram, DFD Level 0 and Level 1).
- **Chapter 4 – Design:** Covers system architecture, API endpoint design, database design (ER diagram, schema tables), UML class and sequence diagrams, and interface wireframes.
- **Chapter 5 – Implementation and Testing:** Details the implementation approach, code structure, charge calculation logic, code efficiency, testing strategy (unit, integration, beta), modifications made during development, and test cases.
- **Chapter 6 – Results and Discussion:** Presents the test report summary and complete user documentation.
- **Chapter 7 – Conclusions:** Summarizes conclusions, the significance of the system, current limitations, and future scope for extension.

---

# CHAPTER 2: SURVEY OF TECHNOLOGIES

## 2.1 Review of Similar/Relevant Projects

Before building NEPSE Pro, we studied what already exists in the market to understand the gap our project fills.

**Table 2.1 – Comparison of Existing NEPSE Platforms**

| Platform | Features Offered | Limitations |
|---|---|---|
| Official NEPSE Website (nepalstock.com) | Contains all official data, trustworthy information | Very complicated to use, looks old-fashioned, hard for beginners, no personal features like watchlist or portfolio tracking |
| Merolagani.com | Shows news, company information, and basic charts | Charts are basic and not interactive; no portfolio management; cluttered with ads; paid services are expensive [14] |
| ShareSansar.com | Provides market news and data | Not mobile-friendly, limited charting features, no personalized experience [15] |
| TradingView (Global) | Professional-grade charting, 100+ indicators, social trading | Does not support NEPSE data natively; no Nepal-specific charge calculation; paid subscription required for full features |

All existing options share one core problem: they treat every visitor the same and provide no personalization. Investors who have been researching stocks for months must start from scratch every visit. None of the Nepal-specific platforms offer portfolio simulation with correct NEPSE charge calculations, professional candlestick charting with technical indicators on NEPSE data, or a combined integrated experience.

NEPSE Pro fills this gap by combining the best real-time NEPSE data with modern, personalized features — candlestick charts, technical indicators, a saved watchlist, and a portfolio simulator with accurate Nepal-specific charge calculation — all in one accessible platform.

---

## 2.2 Technologies Used

### Frontend Stack

| Technology | Version | Purpose |
|---|---|---|
| React [3] | 19.2 | UI component framework |
| TypeScript | 6.0 | Static type safety |
| Vite | 8.0 | Build tool and development server |
| Tailwind CSS [5] | 4.2 | Utility-first styling framework |
| React Router DOM | 7.0 | Client-side routing |
| Lightweight Charts [6] | 4.1 | Interactive candlestick financial charting |
| Axios | 1.15 | HTTP client for API calls |
| Lucide React | 1.8 | Icon library |

### Backend Stack

| Technology | Version | Purpose |
|---|---|---|
| Node.js | 22.12 | JavaScript runtime |
| Express.js [4] | 5.2 | HTTP server and routing framework |
| TypeScript | 6.0 | Type safety across the codebase |
| SQLite (via sqlite3) | 6.0 | Embedded relational database |
| JSON Web Token (JWT) | 9.0 | Stateless authentication tokens |
| Bcryptjs | 3.0 | Secure password hashing (cost factor 12) |
| Passport.js | 0.7 | Google OAuth 2.0 middleware |
| Nodemailer | 8.0 | Transactional email via Gmail SMTP |
| @rumess/nepse-api [2] | 1.0.5 | NEPSE live market data integration |
| tsx | 4.21 | TypeScript runner for development |

### Infrastructure & Deployment

| Service | Purpose |
|---|---|
| Vercel [8] | Frontend deployment on global CDN |
| Render.com | Backend API server hosting |
| Gmail SMTP | Transactional email — OTP and welcome emails |
| MSG91 | SMS OTP delivery for mobile verification |
| Google OAuth 2.0 | Third-party single sign-on authentication |
| GitHub | Source code version control |

---

# CHAPTER 3: REQUIREMENTS AND ANALYSIS

## 3.1 Problem Definition

The current state of NEPSE stock data tools is fragmented and inadequate for the average retail investor in Nepal. Platforms like Merolagani [14], ShareSansar [15], and the official NEPSE website [1] provide basic price listings and news but fall well short of what modern investors need. The core problems are:

**1. Data is hard to understand:** Raw stock prices mean nothing to most people. Seeing "NBL at Rs. 450" does not tell you if that is good or bad. Investors need visual charts to understand price movements and trends.

**2. No personal tracking:** Investors must manually maintain Excel sheets or notebooks to track which stocks they own and at what price. This is messy, error-prone, and does not account for the real cost of transactions (brokerage, SEBON fees, taxes).

**3. No easy watchlist:** When researching, investors find interesting companies but have no way to save them for quick reference on their next visit. Every session starts from scratch.

**4. No charge-aware portfolio simulation:** No free existing platform automatically calculates the real cost of NEPSE trades — including the tiered broker commission structure, SEBON regulatory fees, DP charges, and capital gains tax — so investors have no accurate picture of their true returns.

**5. Complex interface:** Existing websites display too much raw technical information that confuses beginners. A person looking to invest their savings finds it overwhelming.

**6. Not mobile-friendly:** Most existing tools work only on desktop computers. People want to check the market on their phones while traveling or at work [12].

---

## 3.2 Requirements Specification

### Functional Requirements

**Table 3.1 – Functional Requirements**

| FR ID | Requirement | Priority |
|---|---|---|
| FR-01 | User Registration with name, email, password, and mobile number | High |
| FR-02 | Email OTP verification before account activation | High |
| FR-03 | User Login with email and password after email verification | High |
| FR-04 | Google OAuth 2.0 single sign-on login | Medium |
| FR-05 | Display NEPSE index value, point change, and percentage change | High |
| FR-06 | Display market summary (turnover, market cap, traded volume, transactions) | High |
| FR-07 | Display Top Gainers and Top Losers | High |
| FR-08 | Full market watch table with search and sort capabilities | High |
| FR-09 | Candlestick charts for any NEPSE-listed security | High |
| FR-10 | Chart timeframes: 1m, 5m, 15m, 1h, 4h, 1D, 1W, 1M | High |
| FR-11 | Overlay technical indicators: SMA, EMA, RSI, MACD | Medium |
| FR-12 | Configurable indicator parameters (period, color) | Medium |
| FR-13 | Add/remove stocks from personal watchlist | High |
| FR-14 | Live watchlist prices refreshed every 30 seconds | High |
| FR-15 | Simulate buying stocks with virtual cash balance | High |
| FR-16 | Simulate selling held stocks | High |
| FR-17 | Automatic calculation of broker commission, SEBON fee, DP charge, CGT | High |
| FR-18 | View holdings, average buy price, and unrealized P&L | High |
| FR-19 | View full transaction history | Medium |
| FR-20 | Stock search by symbol or company name across all NEPSE listings | High |
| FR-21 | Edit user profile (name, email, mobile, bio) | Low |
| FR-22 | Change account password | Low |
| FR-23 | Logout | High |

### Requirement Prioritization Table

**Table 3.2 – Requirement Prioritization Table**

| Requirement | Priority | Justification |
|---|---|---|
| Real-Time Stock Price Display | High | Core function; primary reason users visit the platform |
| NEPSE Index & Sub-Index View | High | Essential market overview; mandatory for any stock tool |
| Historical Price Charts | High | Required for trend analysis and investment decisions via Lightweight Charts [6] |
| Portfolio Management Module | High | Differentiates this tool from simple price-listing sites |
| Top Gainers / Losers | High | Quick daily market overview; expected by all investors |
| Stock Search by Name/Symbol | High | Critical for navigation with hundreds of listed companies |
| Watchlist Feature | High | Allows personalized tracking; saves users repeated searching |
| Charge Calculation (Nepal-specific) | High | Unique feature not found in any free existing platform |
| Technical Indicators (SMA/EMA/RSI/MACD) | Medium | Useful for advanced users; not critical for all visitors |
| Google OAuth Login | Medium | Useful for convenience; email login covers the core need |
| Sector-Wise Analysis View | Medium | Improves depth of analysis; can be added in a later phase |
| Company Financials Summary | Medium | Useful for fundamental analysis; future enhancement |
| Responsive Design (Mobile) | High | Most users in Nepal access the internet via mobile |

### Non-Functional Requirements

**Table 3.3 – Non-Functional Requirements**

| NFR ID | Requirement | Target Metric |
|---|---|---|
| NFR-01 | Performance — market data response time | Under 2 seconds with API caching |
| NFR-02 | Security — passwords must be hashed | bcrypt with cost factor 12 |
| NFR-03 | Security — JWT tokens must expire | 7-day expiry |
| NFR-04 | Security — OTP must expire | 10-minute expiry |
| NFR-05 | Availability | Pages load within 3–5 seconds on normal internet |
| NFR-06 | Data Accuracy | Stock data must match official NEPSE data |
| NFR-07 | Reliability | System handles errors gracefully without crashing |
| NFR-08 | Responsiveness | App works well on both desktop and mobile screens |
| NFR-09 | Maintainability | Code is well-organized in TypeScript for future updates |
| NFR-10 | Charge Accuracy | Charge calculations must match SEBON official formula exactly |

---

## 3.3 Planning and Scheduling

The project was planned and executed over a period of approximately one month, from mid-May to mid-June 2025, following the schedule described below.

**Figure 3.1 – Gantt Chart**

> *(Insert the Gantt chart figure here. Design it with the tasks and dates described below.)*

The project schedule is as follows. The **Requirement Analysis** phase ran from **May 15 to May 19**, where the initial system needs were identified based on the proposal. This was immediately followed by the **Design** phase, which ran until **May 23** and focused on outlining the system architecture, database schema, and UI wireframes. After the design was completed, three development workstreams started simultaneously on **May 23**: **Frontend Development** (concluded May 31), **Database Integration** (concluded May 28), and **Backend Development** (concluded June 2). **Testing and Debugging** ran concurrently from May 23 through all development activities. The system entered the **Deployment** phase from **June 9 to June 12**, during which the application was hosted on Vercel and Render and made operational. Finally, the **Final Review and Documentation** phase ran from **June 12 to June 14** to assess outcomes and finalize the project report.

---

## 3.4 Software and Hardware Requirements

### Software Requirements

**Table 3.4 – Software Requirements**

| Category | Requirement |
|---|---|
| Development OS | Windows 10/11, macOS, or Linux |
| Runtime | Node.js v22.12.0 |
| Package Manager | npm v10+ |
| Version Control | Git / GitHub |
| Code Editor | Visual Studio Code |
| API Testing | Postman / Thunder Client |
| Browser (Testing) | Google Chrome, Firefox, Safari (latest versions) |
| Design Tool | Figma [11] (free tier — wireframing and mockups) |
| Database Viewer | DB Browser for SQLite |

### Hardware Requirements

**Table 3.5 – Hardware Requirements**

| Component | Minimum | Used (Development) |
|---|---|---|
| Processor | Dual-core 2.0 GHz | Personal laptops (existing) |
| RAM | 4 GB | 8 GB+ |
| Storage | 10 GB free | SSD — sufficient |
| Network | Broadband internet | Home broadband / mobile data |
| Display | 1280×720 | 1920×1080 |

### Detail Budget

**Table 3.6 – Development Cost Estimation**

| Item | Description | Estimated Cost |
|---|---|---|
| Development Effort | 3 members × 120 hrs (academic project) | Rs. 0 |
| Laptop / PC Usage | Personal laptops used for development and testing | Rs. 0 |
| Internet Charges | Home broadband / mobile data for development | Rs. 0 |
| Software Tools | VS Code, Git, Node.js, React, Vite, Tailwind [5] (all free/open source) | Rs. 0 |
| UI/UX Design Tools | Figma [11] free tier for wireframing and mockups | Rs. 0 |
| Hosting / Deployment | Vercel [8] free tier — sufficient for academic project | Rs. 0 |
| Database | SQLite embedded database — no external service required | Rs. 0 |
| Domain Registration | Using Vercel subdomain (nepse-pro.vercel.app) | Rs. 0 |
| Printing & Documentation | Report printing (approx. 50 pages × Rs. 5) + binding | Rs. 500 |
| **Total** | | **Rs. 500** |

All hardware costs are minimized because existing personal devices were used. Open-source technologies (React, Express.js, SQLite, TypeScript, Tailwind CSS) eliminate all software licensing costs. The only real expenditure is report printing and binding.

---

## 3.5 Preliminary Product Description

NEPSE Pro is a web-based stock market analysis and portfolio management platform consisting of two primary components:

### Backend — REST API Server

An Express.js [4] REST API server written in TypeScript, running on Node.js 22, using SQLite as the persistent database via the `sqlite` and `sqlite3` npm packages. The server exposes REST endpoints organized under three route prefixes: `/api/auth` (authentication), `/api/nepse` (market data), and `/api/user` (user-specific data). It integrates with the `@rumess/nepse-api` library [2] to fetch live NEPSE data, and caches API responses in memory (5-second TTL for most endpoints, 60-second TTL for the NEPSE index) to minimize external API dependency. User passwords are hashed with bcrypt (cost factor 12). Authentication uses JWT tokens with a 7-day expiry, verified by a dedicated `authMiddleware` on all protected routes. Google OAuth 2.0 is handled by Passport.js. Transactional emails (OTP, welcome) are sent via Nodemailer with Gmail SMTP.

### Frontend — React Single-Page Application

A single-page application (SPA) built with React 19 [3], TypeScript, and Vite, styled with Tailwind CSS 4. The application communicates with the backend exclusively through REST API calls using a custom `authFetch` wrapper that automatically attaches JWT Bearer tokens and handles session expiry. The application has protected routes managed by an `Auth Guard` component that checks `localStorage` for a valid token before allowing access. Public pages (About, Terms, Disclaimer, How to Use) are accessible without authentication through a `PublicHeader` layout. The main authenticated layout uses a persistent sidebar with navigation to Dashboard, Chart, Market Watch, Portfolio, Watchlist, and Profile pages.

### Project File Structure

```
nepse-pro/
├── backend/
│   ├── src/
│   │   ├── index.ts              ← Express app, middleware, server startup
│   │   ├── db.ts                 ← SQLite initialization, migrations, seeding
│   │   ├── middleware/auth.ts    ← JWT verification middleware
│   │   ├── routes/
│   │   │   ├── authRoutes.ts     ← Registration, OTP, login, Google OAuth
│   │   │   ├── nepseRoutes.ts    ← All NEPSE market data + in-memory cache
│   │   │   └── userRoutes.ts     ← Profile, watchlist, portfolio, trading
│   │   ├── services/
│   │   │   └── portfolioService.ts ← Core business logic (FIFO, P&L, trades)
│   │   ├── types/portfolio.ts    ← TypeScript interfaces for portfolio domain
│   │   └── utils/
│   │       └── chargeCalculator.ts ← NEPSE charge calculation functions
│   └── package.json
└── frontend/
    ├── src/
    │   ├── App.tsx               ← Root router with auth guard
    │   ├── apiConfig.ts          ← API base URLs + authFetch wrapper
    │   ├── pages/
    │   │   ├── auth/             ← Login, Signup, GoogleCallback
    │   │   ├── Dashboard.tsx
    │   │   ├── ChartPage.tsx
    │   │   ├── MarketWatch.tsx
    │   │   ├── Portfolio.tsx
    │   │   ├── Watchlist.tsx
    │   │   └── Profile.tsx
    │   ├── components/
    │   │   ├── Chart/TVChart.tsx  ← Core charting component
    │   │   ├── Portfolio/         ← Trade form, holdings, history components
    │   │   ├── Layout.tsx         ← Authenticated sidebar layout
    │   │   ├── StockSearch.tsx    ← Universal stock search dropdown
    │   │   └── PublicHeader.tsx   ← Unauthenticated page header
    │   └── utils/chargeCalculator.ts ← Frontend charge preview
    └── package.json
```

---

## 3.6 Conceptual Models

### 3.6.1 Use Case Diagram

**Figure 3.2 – Use Case Diagram of NEPSE Pro**

> *(Insert Use Case Diagram figure here — draw using draw.io, Lucidchart, or Figma.)*

**Design specification:**

```
System boundary: "NEPSE Pro Web Application"

Actors:
  • Guest User (unauthenticated)
  • Registered User (authenticated, extends Guest User)
  • NEPSE API (external system — provides market data)

Guest User use cases:
  - Register Account
  - Login (Email/Password)
  - Login with Google (via Google OAuth)
  - View Dashboard (read-only market overview)
  - View Public Pages (About, Terms, Disclaimer, How to Use)

Registered User use cases (all Guest cases, plus):
  - View Dashboard (personalized greeting + live data)
  - View Full Market Watch (search, sort all scrips)
  - Search Stock by Symbol / Company Name
  - View Candlestick Chart (any symbol)
  - Add / Remove Technical Indicators
  - Add Stock to Watchlist
  - Remove Stock from Watchlist
  - View Live Watchlist Prices
  - Execute Virtual Buy Trade
  - Execute Virtual Sell Trade
  - View Holdings and P&L
  - View Transaction History
  - Edit Profile
  - Change Password
  - Logout

«include» relationships:
  - Execute Virtual Buy Trade «include» Login
  - Execute Virtual Sell Trade «include» Login
  - Manage Watchlist «include» Login
  - View Portfolio «include» Login
  - View Transaction History «include» Login
  - Edit Profile «include» Login

NEPSE API (external actor) interacts with:
  - View Dashboard
  - View Full Market Watch
  - View Candlestick Chart
  - View Live Watchlist Prices
```

---

### 3.6.2 Data Flow Diagram — Level 0 (Context Diagram)

**Figure 3.3 – DFD Level 0 (Context Diagram) of NEPSE Pro**

> *(Insert DFD Level 0 figure here — draw using draw.io or any DFD tool.)*

**Design specification:**

```
External Entities:
  1. User (browser — guest or registered)
  2. NEPSE API (external market data source — @rumess/nepse-api)
  3. Gmail SMTP Server (transactional email delivery)
  4. MSG91 (SMS OTP delivery service)
  5. Google OAuth 2.0 (third-party authentication provider)

Central Process:
  ┌──────────────────────────────┐
  │    NEPSE Pro System          │
  │  (single process bubble)     │
  └──────────────────────────────┘

Data flows INTO NEPSE Pro System:
  From User:
    - Registration details (name, email, password, mobile)
    - Email OTP code
    - Login credentials (email/password)
    - Google OAuth token
    - Stock symbol search query
    - Watchlist add/remove requests
    - Virtual trade orders (symbol, quantity, price, type)
    - Profile update data
    - Password change request

  From NEPSE API:
    - Live index data (currentValue, change, percentChange)
    - Market summary (turnover, market cap, volume)
    - Top gainers and losers list
    - All securities list
    - Historical OHLCV data per symbol
    - Intraday tick data per symbol

  From Google OAuth:
    - User profile (name, email, googleId)

Data flows OUT of NEPSE Pro System:
  To User:
    - JWT authentication token
    - Registration confirmation / OTP verification result
    - Dashboard data (index, summary, gainers, losers)
    - Full market watch data
    - Chart OHLCV candle data + computed indicator values
    - Watchlist with live prices
    - Portfolio summary (holdings, P&L, cash balance)
    - Transaction history
    - Trade confirmation with charge breakdown
    - Profile data

  To Gmail SMTP:
    - OTP email (6-digit code, 10-minute expiry)
    - Welcome email (on first Google login)

  To MSG91:
    - SMS OTP request

  To Google OAuth:
    - OAuth authorization request (redirect)
```

---

### 3.6.3 Data Flow Diagram — Level 1

**Figure 3.4 – DFD Level 1 of NEPSE Pro**

> *(Insert DFD Level 1 figure here — draw using draw.io or any DFD tool.)*

**Design specification:**

```
Sub-Processes:
  P1 – User Authentication & Account Management
  P2 – NEPSE Market Data Fetching & Caching
  P3 – Chart Data Processing & Indicator Computation
  P4 – Portfolio & Trade Execution Engine
  P5 – Watchlist Management
  P6 – Nepal Transaction Charge Calculator

Data Stores:
  D1 – Users DB (SQLite: id, name, email, passwordHash, googleId,
                  isVerified, cashBalance, OTP fields, createdAt)
  D2 – Portfolio DB (SQLite: id, user_id, symbol, quantity,
                     buy_price, buy_date, reference)
  D3 – Watchlist DB (SQLite: id, user_id, symbol)
  D4 – Transactions DB (SQLite: id, user_id, symbol, quantity,
                        price, type, createdAt)
  D5 – API Cache (in-memory: cache key → {data, timestamp, TTL})

Key Data Flows:
  User → P1: registration form / OTP code / login credentials / Google token
  P1 ↔ D1: read/write user records, OTP fields, verification status
  P1 → Gmail SMTP: OTP email (fire-and-forget async)
  P1 → MSG91: SMS OTP request
  P1 ↔ Google OAuth: OAuth handshake + profile retrieval
  P1 → User: JWT token + user object

  User → P2: request for index / summary / gainers / live market
  P2 ↔ D5: check cache (TTL); populate if miss
  NEPSE API → P2: raw market data on cache miss
  P2 → User: formatted market data (index, summary, scrips)

  User → P3: symbol + selected timeframe
  P3 ↔ NEPSE API: historical OHLCV + intraday tick data
  P3 → P3: aggregate to timeframe buckets; compute SMA/EMA/RSI/MACD
  P3 → User: OHLCV candle array + indicator value arrays

  User → P4: virtual trade order (symbol, quantity, price, BUY/SELL)
  P4 → P6: send transaction amount + holding info for charge computation
  P6 → P4: ChargeBreakdown {commission, sebonFee, dpCharge, cgt, finalAmount}
  P4 ↔ D1: read/update user cashBalance
  P4 ↔ D4: INSERT transaction record
  P4 ↔ D3: (check holdings for SELL validation)
  P4 → User: trade confirmation + charge breakdown + updated balance

  User → P5: add or remove symbol from watchlist
  P5 ↔ D3: read/write watchlist records
  P5 → P2: request live prices for all watchlist symbols
  P5 → User: watchlist symbols + live prices + percentage change
```

---

# CHAPTER 4: DESIGN

## 4.1 Introduction

NEPSE Pro follows a client-server architecture with a clear separation between the React frontend presentation layer and the Express.js backend business logic layer. The database layer uses SQLite for embedded file-based persistence, which is appropriate for the project's current scale. The frontend is served from Vercel's global CDN, and the backend API runs on Render's cloud infrastructure — both connected securely over HTTPS.

---

## 4.2 System Design

**Figure 4.1 – System Architecture Diagram**

> *(Insert System Architecture figure here.)*

**Design specification:**

```
[Client Layer — Vercel CDN]
  Browser → React 19 SPA
    ├── React Router (10 client-side routes)
    ├── Auth Guard (localStorage JWT check)
    ├── authFetch wrapper (auto-attaches Bearer token)
    ├── Lightweight Charts (candlestick rendering + indicators)
    └── Tailwind CSS (dark-theme responsive layout)
              │ HTTPS + JWT Bearer Token
              ▼
[API Server Layer — Render.com, Port 5000]
  Express.js v5 Application
    ├── CORS Middleware (origin: '*')
    ├── JSON Body Parser
    ├── Express Session
    ├── Passport.js (Google OAuth 2.0)
    ├── authMiddleware (JWT verification → req.userId)
    └── Route Handlers:
          /api/auth  → authRoutes.ts
          /api/nepse → nepseRoutes.ts (+ in-memory cache D5)
          /api/user  → userRoutes.ts
          /api/health → health check
              │
[Service & Utility Layer]
  PortfolioService   ← FIFO cost basis, P&L, trade execution
  ChargeCalculator   ← broker commission, SEBON, DP, CGT
  OTP Generator      ← cryptographic 6-digit random
  Email Service      ← Nodemailer + Gmail SMTP (IPv4 forced)
  SMS Service        ← MSG91 REST API
  API Cache          ← in-memory Map {key: {data, ts}}
              │
[Database Layer]
  SQLite (nepse.db — local file)
    ├── users        (D1)
    ├── portfolio    (D2)
    ├── watchlist    (D3)
    └── transactions (D4)
              │
[External Services]
  @rumess/nepse-api → NEPSE real-time data
  Google OAuth 2.0  → third-party SSO
  Gmail SMTP        → email OTP delivery
  MSG91             → SMS OTP delivery
```

### API Endpoints

**Table 4.1 – API Endpoints: Authentication**

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/signup/init` | No | Register user; send email OTP |
| POST | `/api/auth/verify/email` | No | Verify email OTP; receive JWT |
| POST | `/api/auth/resend/email-otp` | No | Resend email OTP |
| POST | `/api/auth/send/sms-otp` | No | Send SMS OTP |
| POST | `/api/auth/verify/sms` | No | Verify SMS OTP |
| POST | `/api/auth/login` | No | Login with email + password |
| GET | `/api/auth/me` | Bearer JWT | Get current user info from token |
| GET | `/api/auth/google` | No | Initiate Google OAuth flow |
| GET | `/api/auth/google/callback` | No | Google OAuth redirect callback |

**Table 4.2 – API Endpoints: NEPSE Market Data**

| Method | Endpoint | Auth | Cache TTL | Description |
|---|---|---|---|---|
| GET | `/api/nepse/index` | No | 60 s | NEPSE index (currentValue, change, %) |
| GET | `/api/nepse/summary` | No | 5 s | Market summary (turnover, cap, volume) |
| GET | `/api/nepse/status` | No | 5 s | Market open / closed status |
| GET | `/api/nepse/live` | No | 5 s | Combined gainers + losers data |
| GET | `/api/nepse/gainers` | No | 5 s | Top 10 gainers |
| GET | `/api/nepse/losers` | No | 5 s | Top 10 losers |
| GET | `/api/nepse/turnover` | No | 5 s | Top 10 by turnover |
| GET | `/api/nepse/securities` | No | 5 s | Full NEPSE securities list |
| GET | `/api/nepse/history/:symbol` | No | 5 s | Historical OHLCV data |
| GET | `/api/nepse/intraday/:symbol` | No | 5 s | Today's intraday trade ticks |

**Table 4.3 – API Endpoints: User Management**

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/user/profile` | Bearer JWT | Get user profile |
| PUT | `/api/user/profile` | Bearer JWT | Update profile (name, email, mobile, bio) |
| PUT | `/api/user/password` | Bearer JWT | Change password |
| GET | `/api/user/watchlist` | Bearer JWT | Get all watchlist symbols |
| POST | `/api/user/watchlist` | Bearer JWT | Add symbol to watchlist |
| DELETE | `/api/user/watchlist/:symbol` | Bearer JWT | Remove symbol from watchlist |
| GET | `/api/user/portfolio` | Bearer JWT | Get portfolio summary |
| POST | `/api/user/trade` | Bearer JWT | Execute BUY or SELL trade |
| GET | `/api/user/holdings` | Bearer JWT | Get current holdings (computed from transactions) |
| GET | `/api/user/transactions` | Bearer JWT | Get transaction history |
| GET | `/api/user/cash` | Bearer JWT | Get virtual cash balance |
| PUT | `/api/user/cash` | Bearer JWT | Update virtual cash balance |
| GET | `/api/user/quote` | Bearer JWT | Get trade quote with all charges |

---

## 4.3 Database Design

### Entity-Relationship Diagram

**Figure 4.2 – ER Diagram of NEPSE Pro**

> *(Insert ER Diagram figure here — draw using draw.io, Lucidchart, or ERDPlus.)*

**Design specification:**

```
Entities and Attributes (using Crow's Foot or Chen notation):

┌─────────────────────────────────────┐
│               USERS                 │
├─────────────────────────────────────┤
│ PK  id            INTEGER           │
│     name          TEXT NOT NULL     │
│     email         TEXT UNIQUE NN    │
│     password      TEXT              │
│     mobile        TEXT              │
│     bio           TEXT              │
│     googleId      TEXT              │
│     provider      TEXT ('email'|'google') │
│     isVerified    INTEGER (0|1)     │
│     emailOTP      TEXT              │
│     emailOTPExpiry TEXT             │
│     smsOTP        TEXT              │
│     smsOTPExpiry  TEXT              │
│     cashBalance   REAL DEFAULT 100000 │
│     createdAt     TEXT              │
└──────────────┬──────────────────────┘
               │ 1
    ┌──────────┼────────────────────────┐
    │          │                        │
   many       many                    many
    │          │                        │
    ▼          ▼                        ▼
┌──────────┐  ┌──────────┐  ┌──────────────────┐
│ WATCHLIST│  │PORTFOLIO │  │  TRANSACTIONS    │
├──────────┤  ├──────────┤  ├──────────────────┤
│ PK id    │  │ PK id    │  │ PK id            │
│ FK user_id│ │ FK user_id│ │ FK user_id       │
│ symbol   │  │ symbol   │  │ symbol           │
│ UNIQUE   │  │ name     │  │ quantity (REAL)  │
│(user,sym)│  │ quantity │  │ price    (REAL)  │
└──────────┘  │ buy_price│  │ type (BUY|SELL)  │
              │ buy_date │  │ createdAt        │
              │ reference│  └──────────────────┘
              │ createdAt│
              └──────────┘

All child entities: ON DELETE CASCADE from USERS
```

### Database Schema Tables

**Table 4.4 – Database Schema: Users**

| Column | Type | Constraint | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique user identifier |
| name | TEXT | NOT NULL | User's display name |
| email | TEXT | UNIQUE, NOT NULL | Login email address |
| password | TEXT | DEFAULT NULL | Bcrypt hash (null for Google OAuth users) |
| mobile | TEXT | DEFAULT '' | Mobile phone number |
| bio | TEXT | DEFAULT '' | Short user biography |
| googleId | TEXT | DEFAULT NULL | Google OAuth unique user ID |
| provider | TEXT | DEFAULT 'email' | Authentication provider: 'email' or 'google' |
| isVerified | INTEGER | DEFAULT 0 | Email verification flag (0 = unverified, 1 = verified) |
| emailOTP | TEXT | DEFAULT NULL | 6-digit email verification code |
| emailOTPExpiry | TEXT | DEFAULT NULL | OTP expiry timestamp (ISO 8601) |
| smsOTP | TEXT | DEFAULT NULL | 6-digit SMS verification code |
| smsOTPExpiry | TEXT | DEFAULT NULL | SMS OTP expiry timestamp |
| cashBalance | REAL | DEFAULT 100000 | Virtual trading cash balance in Rs. |
| createdAt | TEXT | DEFAULT datetime('now') | Account creation timestamp |

**Table 4.5 – Database Schema: Portfolio**

| Column | Type | Constraint | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Entry identifier |
| user_id | INTEGER | FK → users.id, ON DELETE CASCADE | Owning user |
| symbol | TEXT | NOT NULL | NEPSE stock symbol (stored uppercase) |
| name | TEXT | DEFAULT '' | Company name |
| quantity | REAL | NOT NULL | Number of shares held |
| buy_price | REAL | NOT NULL | Purchase price per share |
| buy_date | TEXT | DEFAULT '' | Purchase date |
| reference | TEXT | DEFAULT '' | Reference or broker note |
| createdAt | TEXT | DEFAULT datetime('now') | Record creation time |

**Table 4.6 – Database Schema: Watchlist**

| Column | Type | Constraint | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Entry identifier |
| user_id | INTEGER | FK → users.id, ON DELETE CASCADE | Owning user |
| symbol | TEXT | NOT NULL | NEPSE stock symbol (uppercase) |
| — | — | UNIQUE(user_id, symbol) | One symbol per user only |

**Table 4.7 – Database Schema: Transactions**

| Column | Type | Constraint | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Transaction identifier |
| user_id | INTEGER | FK → users.id, ON DELETE CASCADE | Owning user |
| symbol | TEXT | NOT NULL | Stock symbol (uppercase) |
| quantity | REAL | NOT NULL | Number of shares in this transaction |
| price | REAL | NOT NULL | Per-share price at execution |
| type | TEXT | CHECK (IN ('BUY', 'SELL')) | Transaction direction |
| createdAt | TEXT | DEFAULT datetime('now') | Execution timestamp |

---

## 4.4 Interface Design

### UML Class Diagram

**Figure 4.3 – UML Class Diagram of NEPSE Pro**

> *(Insert UML Class Diagram figure here — draw using draw.io, StarUML, or Lucidchart.)*

**Design specification:**

```
Classes:

┌──────────────────────────────────────────┐
│              PortfolioService            │
├──────────────────────────────────────────┤
│ - db: Database                           │
├──────────────────────────────────────────┤
│ + getCashBalance(userId: number): Promise<number>          │
│ + setCashBalance(userId, amount): Promise<boolean>         │
│ + getTransactions(userId, order): Promise<Transaction[]>   │
│ + getHoldings(userId): Promise<Holding[]>                  │
│ + getTradeQuote(userId, symbol, qty, price, type):         │
│     Promise<TradeQuote>                                    │
│ + executeTrade(userId, symbol, qty, price, type):          │
│     Promise<Transaction>                                   │
│ + getRealizedMetrics(userId): Promise<RealizedPLMetrics>   │
│ + getPortfolioSummary(userId): Promise<PortfolioSummary>   │
│ - buildPortfolioState(txns): PortfolioState                │
└──────────────────────────────────────────┘
           «uses»
┌──────────────────────────────────────────┐
│           ChargeCalculator               │
├──────────────────────────────────────────┤
│ + DP_CHARGE: number = 25                 │
├──────────────────────────────────────────┤
│ + calculateBrokerCommission(amount): number                │
│ + calculateSebonFee(amount): number                        │
│ + calculateCapitalGainsTax(profit, purchaseDate,           │
│     saleDate): number                                      │
│ + calculateBuyCost(amount): ChargeBreakdown                │
│ + calculateSellProceeds(saleAmount, purchaseCost,          │
│     purchaseDate, saleDate): ChargeBreakdown               │
└──────────────────────────────────────────┘

Key Interfaces (TypeScript):
  Transaction    { id, user_id, symbol, quantity, price, type, createdAt }
  Holding        { symbol, quantity, avgBuyPrice, totalInvested, avgPurchaseDate }
  TradeQuote     { type, symbol, quantity, price, subtotal, charges, total, projectedBalance }
  ChargeBreakdown { transactionAmount, brokerCommission, sebonFee, dpCharge,
                    capitalGainsTax, totalCost, finalAmount }
  PortfolioSummary { cashBalance, totalInvested, holdings, transactions }
```

### UML Sequence Diagrams

**Figure 4.4 – Sequence Diagram: User Registration and Email Verification**

> *(Insert UML Sequence Diagram figure here.)*

**Design specification:**

```
Lifelines (left to right):
  User | React Frontend | Express Backend | SQLite DB | Gmail SMTP

1. User → Frontend: Fill registration form (name, email, password, mobile)
2. Frontend → Backend: POST /api/auth/signup/init {name, email, password, mobile}
3. Backend → DB: SELECT id, isVerified FROM users WHERE email = ?
4. DB → Backend: No existing record (or unverified — deleted)
5. Backend → Backend: bcrypt.hash(password, 12)
6. Backend → Backend: generateOTP() → 6-digit code; set expiry = now + 10 min
7. Backend → DB: INSERT INTO users (name, email, passwordHash, emailOTP, emailOTPExpiry)
8. Backend → Gmail SMTP: sendEmailOtp(email, otp) [async, fire-and-forget]
9. Backend → Frontend: 201 {userId, email, requiresVerification: true}
10. Frontend → User: Show OTP input screen
11. User → Frontend: Enter 6-digit OTP
12. Frontend → Backend: POST /api/auth/verify/email {userId, otp}
13. Backend → DB: SELECT emailOTP, emailOTPExpiry, isVerified FROM users WHERE id = ?
14. Backend → Backend: Check OTP match + check expiry < now
15. Backend → DB: UPDATE users SET isVerified=1, emailOTP=NULL, emailOTPExpiry=NULL
16. Backend → Backend: jwt.sign({userId, email}, JWT_SECRET, {expiresIn: '7d'})
17. Backend → Frontend: 200 {token, user}
18. Frontend → Frontend: localStorage.setItem('token', token)
19. Frontend → User: Navigate to /dashboard
```

**Figure 4.5 – Sequence Diagram: Virtual Trade Execution (BUY)**

> *(Insert UML Sequence Diagram figure here.)*

**Design specification:**

```
Lifelines (left to right):
  User | Portfolio Page | Backend API | PortfolioService | ChargeCalculator | SQLite DB

1. User → Portfolio Page: Open trade form; enter symbol, quantity, price; choose BUY
2. Portfolio Page → Backend API: POST /api/user/trade {symbol, qty, price, type: 'BUY'}
   [Authorization: Bearer <JWT>]
3. Backend API → Backend API: authMiddleware: jwt.verify(token) → req.userId
4. Backend API → PortfolioService: executeTrade(userId, symbol, qty, price, 'BUY')
5. PortfolioService → DB: SELECT cashBalance FROM users WHERE id = userId
6. DB → PortfolioService: cashBalance = Rs. X
7. PortfolioService → ChargeCalculator: calculateBuyCost(qty × price)
8. ChargeCalculator → PortfolioService: {brokerCommission, sebonFee, finalAmount}
9. PortfolioService → PortfolioService: if (cashBalance < finalAmount) → throw Error
10. PortfolioService → DB: UPDATE users SET cashBalance = cashBalance - finalAmount
11. PortfolioService → DB: INSERT INTO transactions (user_id, symbol, qty, price, 'BUY')
12. DB → PortfolioService: {lastID}
13. PortfolioService → Backend API: Transaction object
14. Backend API → Portfolio Page: 201 {transaction, tradeQuote with charge breakdown}
15. Portfolio Page → User: Show success toast + updated holdings table
```

---

## 4.5 Summary

The design of NEPSE Pro establishes a clean three-tier client-server architecture. The backend follows a route → middleware → service pattern, with `PortfolioService` encapsulating all core business logic (FIFO cost basis, P&L, trade execution, balance management) and `ChargeCalculator` implementing Nepal-specific NEPSE transaction costs. The database design is minimal (4 tables) and normalized, with all user data cascaded on account deletion for data integrity. The frontend is a component-based React SPA with protected routes, a dark professional UI, and all technical indicator computations performed client-side to minimize server load.

---

# CHAPTER 5: IMPLEMENTATION AND TESTING

## 5.1 Implementation Approaches

### 5.1.1 Frontend Architecture

The frontend is organized into three layers: page components (route-level), reusable UI components, and utility functions.

**Route and Auth Guard Pattern**

The root `App.tsx` defines all routes. A `Guard` component wraps all authenticated routes and checks `localStorage` for a JWT token before rendering. If no token is found, the user is redirected to `/login`. A guest mode (`localStorage.getItem('guest') === 'true'`) allows limited dashboard-only read access without registration.

```typescript
const Guard = ({ children }) => {
  const isGuest = localStorage.getItem('guest') === 'true';
  if (isAuth()) return <>{children}</>;
  if (isGuest && location.pathname === '/dashboard') return <>{children}</>;
  return <Navigate to={isGuest ? '/signup' : '/login'} replace />;
};
```

**`authFetch` Wrapper**

All authenticated API calls use a custom `authFetch` function that automatically appends the `Authorization: Bearer <token>` header and handles 401 responses by clearing the token and redirecting to `/login`:

```typescript
export async function authFetch(url: string, options: RequestInit = {}): Promise<Response> {
  const token = localStorage.getItem('token');
  const headers = { ...(options.headers || {}), ...(token ? { Authorization: `Bearer ${token}` } : {}) };
  if (options.body) headers['Content-Type'] = 'application/json';
  const res = await fetch(url, { ...options, headers });
  if (res.status === 401) {
    localStorage.removeItem('token');
    window.location.href = '/login';
  }
  return res;
}
```

### 5.1.2 Backend Architecture

**Express Server Setup (`index.ts`)**

The server configures: CORS (all origins), JSON body parser, express-session, and Passport.js for OAuth. The `initDb()` function is called at startup to ensure all tables exist and migrations are applied. Four route groups are registered.

**Database Initialization (`db.ts`)**

The `initDb()` function creates all four tables using `CREATE TABLE IF NOT EXISTS`, then iterates through a migration array of `ALTER TABLE` statements (each wrapped in try/catch to silently skip already-existing columns). A demo user is seeded if the database is empty, providing a working account (`demo@example.com` / `password`) for first-time testing.

**JWT Authentication Middleware (`auth.ts`)**

```typescript
export const authMiddleware = (req: AuthRequest, res: Response, next: NextFunction): void => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) { res.status(401).json({ error: 'Unauthorized: No token provided' }); return; }
  try {
    const decoded = jwt.verify(token, JWT_SECRET) as { userId: number; email: string };
    req.userId = decoded.userId;
    req.userEmail = decoded.email;
    next();
  } catch {
    res.status(401).json({ error: 'Unauthorized: Invalid or expired token' });
  }
};
```

**In-Memory API Cache (`nepseRoutes.ts`)**

NEPSE API responses are cached in a simple in-memory object to avoid hammering the external API:

```typescript
const cache: Record<string, { data: any; ts: number }> = {};
const cached = async <T>(key: string, fn: () => Promise<T>, ttlMs = 5000): Promise<T> => {
  if (cache[key] && Date.now() - cache[key].ts < ttlMs) return cache[key].data as T;
  const data = await fn();
  cache[key] = { data, ts: Date.now() };
  return data;
};
```

---

## 5.2 Coding Details and Code Efficiency

### 5.2.1 Code Efficiency

**Nepal-Specific Broker Commission — 5-Tier Structure**

NEPSE Pro implements the official SEBON broker commission structure exactly:

**Table 5.1 – Broker Commission Tier Structure**

| Transaction Amount (Rs.) | Commission Rate |
|---|---|
| Up to 50,000 | 0.36% |
| 50,001 to 5,00,000 | 0.33% |
| 5,00,001 to 20,00,000 | 0.31% |
| 20,00,001 to 1,00,00,000 | 0.27% |
| Above 1,00,00,000 | 0.24% |

```typescript
export function calculateBrokerCommission(amount: number): number {
  if (amount <= 50000)    return amount * 0.0036;
  if (amount <= 500000)   return amount * 0.0033;
  if (amount <= 2000000)  return amount * 0.0031;
  if (amount <= 10000000) return amount * 0.0027;
  return amount * 0.0024;
}
```

**SEBON Regulatory Fee**

```typescript
export function calculateSebonFee(amount: number): number {
  return amount * 0.00015;  // 0.015% of transaction amount
}
```

**Capital Gains Tax Calculation**

```typescript
export function calculateCapitalGainsTax(
  profit: number, purchaseDate: Date, saleDate: Date
): number {
  if (profit <= 0) return 0; // No tax on loss or break-even
  const days = Math.floor((saleDate.getTime() - purchaseDate.getTime()) / 86400000);
  const taxRate = days < 365 ? 0.075 : 0.05; // 7.5% short-term; 5% long-term
  return profit * taxRate;
}
```

**Buy Cost Calculation**

```typescript
export function calculateBuyCost(amount: number): ChargeBreakdown {
  const brokerCommission = calculateBrokerCommission(amount);
  const sebonFee = calculateSebonFee(amount);
  const totalCost = brokerCommission + sebonFee; // No DP charge on BUY
  return { transactionAmount: amount, brokerCommission, sebonFee,
           dpCharge: 0, capitalGainsTax: 0, totalCost,
           finalAmount: amount + totalCost };
}
```

**Sell Proceeds Calculation**

```typescript
export function calculateSellProceeds(
  saleAmount: number, purchaseCost: number,
  purchaseDate: Date, saleDate: Date
): ChargeBreakdown {
  const brokerCommission = calculateBrokerCommission(saleAmount);
  const sebonFee = calculateSebonFee(saleAmount);
  const dpCharge = 25; // Fixed Rs. 25 per sell transaction
  const profit = saleAmount - purchaseCost;
  const capitalGainsTax = calculateCapitalGainsTax(profit, purchaseDate, saleDate);
  const totalCost = brokerCommission + sebonFee + dpCharge + capitalGainsTax;
  return { transactionAmount: saleAmount, brokerCommission, sebonFee,
           dpCharge, capitalGainsTax, totalCost,
           finalAmount: saleAmount - totalCost };
}
```

**FIFO Portfolio Engine (`portfolioService.ts`)**

The `buildPortfolioState()` method processes all transactions in chronological `ASC` order. For each BUY, it updates the running average cost using a weighted average formula. For each SELL, it computes realized P&L against that average cost:

```typescript
if (tx.type === 'BUY') {
  const newQuantity = position.quantity + tx.quantity;
  const newInvested = position.totalInvested + (tx.quantity * tx.price);
  position.avgBuyPrice = newInvested / newQuantity;  // weighted average
  position.quantity = newQuantity;
  position.totalInvested = newInvested;
} else { // SELL
  const soldCostBasis = position.avgBuyPrice * tx.quantity;
  const saleAmount = tx.quantity * tx.price;
  const breakdown = calculateSellProceeds(saleAmount, soldCostBasis, purchaseDate, saleDate);
  realizedPL += breakdown.finalAmount - soldCostBasis;
  position.quantity -= tx.quantity;
  position.totalInvested = position.quantity * position.avgBuyPrice;
}
```

**Technical Indicators (Frontend — Client-Side)**

All four technical indicators are computed entirely in the browser from the raw OHLCV data arrays returned by the API. This removes any server-side computation overhead and allows parameters to be changed and the indicator re-plotted instantly without a new network request.

- **SMA**: Simple rolling average of `close` prices over `period` candles.
- **EMA**: Exponential moving average using multiplier `k = 2 / (period + 1)`, applied iteratively.
- **RSI**: Wilder's smoothing method using rolling average gains and losses over `period` candles.
- **MACD**: Fast EMA (12) minus Slow EMA (26) as the MACD line; Signal line = EMA(9) of MACD line; Histogram = MACD − Signal.

**Real-Time Chart Polling**

The chart component uses `setInterval` (5-second interval) to fetch the latest intraday tick from the NEPSE API and calls `candleSeriesRef.current.update(latestCandle)` — Lightweight Charts' efficient single-candle update method — to extend the current chart without re-rendering the entire dataset.

**Nepal Timezone Handling for Intraday**

```typescript
const nepalOffsetMs = (5 * 60 + 45) * 60 * 1000; // UTC+5:45
const todayDate = new Date(Date.now() + nepalOffsetMs).toISOString().split('T')[0];
```

This ensures the live candle constructed from intraday ticks is assigned the correct Nepal Standard Time date, preventing it from appearing on the wrong day in the chart's time axis.

---

## 5.3 Testing Approach

### 5.3.1 Unit Testing

Unit tests targeted individual isolated functions containing critical business logic. The following functions were tested:

- `calculateBrokerCommission(amount)` — tested at each tier boundary value (Rs. 50,000; Rs. 50,001; Rs. 5,00,000; Rs. 5,00,001; Rs. 20,00,000) to verify tier switching.
- `calculateSebonFee(amount)` — verified as exactly 0.015% of any input amount.
- `calculateCapitalGainsTax(profit, purchaseDate, saleDate)` — tested at 200 days (7.5%), 400 days (5%), and with negative profit (0 tax).
- `calculateBuyCost(amount)` and `calculateSellProceeds(...)` — verified that all components sum correctly to the final amount.
- `buildPortfolioState(transactions)` — tested with multiple BUY + SELL sequences to verify correct average cost basis, realized P&L, and remaining holdings.

### 5.3.2 Integrated Testing

Integration tests verified end-to-end flows through route handlers into the SQLite database. Key scenarios tested:

- Registration → OTP sent → email verification → JWT returned → protected routes accessible.
- Login with correct credentials → JWT returned.
- Login with wrong password → 401.
- Login with unverified account → 403 with `requiresVerification: true`.
- Add watchlist symbol → 201; add duplicate → 409 Conflict.
- POST trade BUY with sufficient balance → transaction recorded, cashBalance reduced.
- POST trade BUY exceeding balance → 400 Insufficient balance error.
- POST trade SELL without holdings → 400 Insufficient shares error.
- Access protected route without token → 401.
- Access protected route with expired/invalid token → 401.

Tools used: Postman for manual API testing; browser DevTools for frontend request verification.

### 5.3.3 Beta Testing

Beta testing was conducted with a small group of target users familiar with NEPSE investing. Key observations:

- **NEPSE Index Discrepancy Found:** Beta testers reported that the displayed NEPSE index value did not match the official NEPSE website. Investigation revealed the bug described in Section 5.4.
- **Charge Calculations Verified:** Beta testers manually computed expected charges for sample transactions and compared with the system output. All calculations matched exactly.
- **UI Usability:** The watchlist and portfolio pages were navigated without instruction. The trade form was understood by all testers.
- **Mobile Compatibility:** All pages were verified functional on Android Chrome and iOS Safari.
- **Watchlist Real-Time Updates:** Confirmed that watchlist prices auto-update every 30 seconds without requiring a page reload.

---

## 5.4 Modifications and Improvements

The following significant issues were identified and resolved during development and beta testing:

**1. NEPSE Index Value Bug (Critical)**
The dashboard was displaying the `close` field from the NEPSE API response (the previous session's closing snapshot) rather than the `currentValue` field (the live session value). This caused the displayed NEPSE index to be one session behind reality. Corrected in `Layout.tsx`, `Dashboard.tsx`, and `HeaderNotifications.tsx`. The fix: `nepseIndex?.currentValue ?? nepseIndex?.close`. The backend index cache TTL was simultaneously extended from 5 seconds to 60 seconds to reduce unnecessary API calls while still maintaining a regularly updated display.

**2. SMTP IPv4 Failure on Render**
Email OTP delivery was failing silently on Render's cloud infrastructure due to IPv6 connectivity issues when reaching Gmail's SMTP servers. Gmail's SMTP resolves to both IPv4 and IPv6 addresses, and Render's infrastructure would attempt the IPv6 connection which then failed with `ENETUNREACH`. Fixed by forcing `family: 4` in the Nodemailer SMTP transport configuration, and implementing automatic retry with port 465 (`secure: true`) if port 587 fails.

**3. Google OAuth Runtime Guard**
If `GOOGLE_CLIENT_ID` or `GOOGLE_CLIENT_SECRET` environment variables are not configured, the Google login route previously caused Passport.js to crash the request. Fixed by adding a runtime environment variable check at the start of the `/api/auth/google` route, returning a clear `503` error with message `"Google login is not configured. Please contact admin."` instead of crashing.

**4. Database Migration System**
Early testing revealed that adding new database columns to an existing SQLite database (for deployed instances that already had the old schema) caused errors. Fixed by implementing a migration array in `initDb()` — each `ALTER TABLE ADD COLUMN` statement is wrapped in a try/catch that silently ignores "column already exists" errors, allowing safe incremental schema evolution without destroying existing data.

**5. "One Day Late" Chart Bug**
Historical OHLCV data from the NEPSE API has a publication lag and does not include the current trading day's candle. This caused the chart to appear to end one day behind the current date. Fixed by simultaneously fetching intraday tick data for the current day, constructing a synthetic live candle from those ticks, and merging it with the historical dataset — overwriting any stale last candle or appending a new one for today with the correct Nepal Standard Time date.

---

## 5.5 Test Cases

**Table 5.2 – Unit Test Cases**

| TC ID | Function | Input | Expected Output | Result |
|---|---|---|---|---|
| UT-01 | `calculateBrokerCommission` | Rs. 50,000 | Rs. 180.00 (0.36%) | Pass |
| UT-02 | `calculateBrokerCommission` | Rs. 50,001 | Rs. 165.00 (0.33%) | Pass |
| UT-03 | `calculateBrokerCommission` | Rs. 5,00,000 | Rs. 1,650.00 (0.33%) | Pass |
| UT-04 | `calculateBrokerCommission` | Rs. 5,00,001 | Rs. 1,550.00 (0.31%) | Pass |
| UT-05 | `calculateSebonFee` | Rs. 1,00,000 | Rs. 15.00 (0.015%) | Pass |
| UT-06 | `calculateCapitalGainsTax` | profit=10,000; days=200 | Rs. 750.00 (7.5%) | Pass |
| UT-07 | `calculateCapitalGainsTax` | profit=10,000; days=400 | Rs. 500.00 (5.0%) | Pass |
| UT-08 | `calculateCapitalGainsTax` | profit=−2,000; days=100 | Rs. 0 (no tax on loss) | Pass |
| UT-09 | `calculateBuyCost` | Rs. 1,00,000 | finalAmount = Rs. 1,00,345 | Pass |
| UT-10 | `buildPortfolioState` | 2× BUY + 1× SELL | Correct avgBuyPrice, realizedPL | Pass |
| UT-11 | `buildPortfolioState` | SELL quantity > held | Throws error | Pass |
| UT-12 | `buildPortfolioState` | Full sell of all shares | Holdings map empty | Pass |

**Table 5.3 – Integration Test Cases**

| TC ID | Endpoint | Method | Scenario | Expected Response | Result |
|---|---|---|---|---|---|
| IT-01 | `/api/auth/signup/init` | POST | Valid new user data | 201 `{userId, requiresVerification: true}` | Pass |
| IT-02 | `/api/auth/signup/init` | POST | Already verified email | 409 Conflict | Pass |
| IT-03 | `/api/auth/verify/email` | POST | Correct OTP within expiry | 200 `{token, user}` | Pass |
| IT-04 | `/api/auth/verify/email` | POST | Expired OTP | 400 'OTP has expired' | Pass |
| IT-05 | `/api/auth/verify/email` | POST | Wrong OTP | 400 'Invalid verification code' | Pass |
| IT-06 | `/api/auth/login` | POST | Valid credentials, verified account | 200 `{token}` | Pass |
| IT-07 | `/api/auth/login` | POST | Wrong password | 401 'Invalid email or password' | Pass |
| IT-08 | `/api/auth/login` | POST | Unverified account | 403 `requiresVerification: true` | Pass |
| IT-09 | `/api/user/watchlist` | POST | Add new symbol (authenticated) | 201 `{id, symbol}` | Pass |
| IT-10 | `/api/user/watchlist` | POST | Add duplicate symbol | 409 Conflict | Pass |
| IT-11 | `/api/user/trade` | POST | BUY with sufficient balance | 201 `{transaction, tradeQuote}` | Pass |
| IT-12 | `/api/user/trade` | POST | BUY exceeding cash balance | 400 'Insufficient balance' | Pass |
| IT-13 | `/api/user/trade` | POST | SELL without any holdings | 400 'Insufficient shares' | Pass |
| IT-14 | `/api/nepse/index` | GET | No parameters | 200 `[{index, currentValue, change}]` | Pass |
| IT-15 | Any protected route | GET | No Authorization header | 401 'No token provided' | Pass |

---

# CHAPTER 6: RESULTS AND DISCUSSION

## 6.1 Test Reports

All unit and integration test cases were executed and all passed. Beta testing with target users passed with one issue identified and subsequently resolved.

**Table 6.1 – Test Report Summary**

| Test Category | Total Cases | Passed | Failed | Pass Rate |
|---|---|---|---|---|
| Unit Tests | 12 | 12 | 0 | 100% |
| Integration Tests | 15 | 15 | 0 | 100% |
| Beta User Tests | 12 | 11 | 1* | 91.6% |

*\*One beta failure: NEPSE index displayed previous close instead of live value — resolved with the bug fix documented in Section 5.4.*

**Key observations from testing:**

- **Charge accuracy:** All broker commission, SEBON fee, DP charge, and CGT calculations matched manual computations using official SEBON formulas within floating-point precision (less than Rs. 0.01 variance for any input).

- **Authentication security:** OTP expiry enforcement correctly rejected codes older than 10 minutes. Bcrypt password hashing with cost factor 12 ensures passwords cannot be reversed from the stored hash.

- **Portfolio consistency:** The FIFO portfolio engine correctly handles full position liquidation (entry removed from holdings), partial sells (quantity decremented, average price preserved), and sequences of multiple buys at different prices followed by partial sells.

- **NEPSE data reliability:** API caching reduced external NEPSE API call frequency by approximately 95% under typical usage, significantly reducing the risk of rate limiting and improving response times.

- **Chart correctness:** The intraday live candle merge correctly applied the Nepal Standard Time offset (UTC+5:45), ensuring today's candle is placed on the correct date in the chart time axis.

- **Performance:** Average API response time observed during testing was under 200 ms for cached NEPSE data endpoints and under 500 ms for database-backed user endpoints — well within the 3–5 second NFR target [10].

- **Responsiveness:** All pages (Dashboard, Chart, Market Watch, Portfolio, Watchlist) rendered correctly and were fully usable on both desktop (1920×1080) and mobile (375×812, iPhone SE viewport) screens.

---

## 6.2 User Documentation

### Getting Started

**Registration**
1. Open `https://nepse-pro.vercel.app` in any modern browser.
2. Click **Sign Up** on the login page.
3. Enter your full name, email address, password (minimum 6 characters), and mobile number.
4. Click **Create Account** — a 6-digit verification code will be sent to your email.
5. Enter the verification code on the next screen. Your account will be activated immediately.
6. Alternatively, click **Continue with Google** on the login page for one-click sign-in using your Google account.

**Login**
1. Enter your registered email and password and click **Login**.
2. Or click **Continue with Google** for Google SSO login.
3. On successful login, you will be redirected to the Dashboard.

---

### Dashboard

The Dashboard is your market overview home screen. It displays:

- **NEPSE Index card:** Live index value, point change, and percentage change since the previous session.
- **Market Summary cards:** Total market turnover (in crores), market capitalization (in trillions), total traded shares, and total transaction count.
- **Top Gainers / Top Losers panels:** The top 6 securities by percentage price increase or decrease today.
- **Live Market Watch table:** A scrollable table of all actively traded securities showing symbol, LTP, price change, percentage change, high, low, and volume.

Click any stock symbol in any table or panel to navigate directly to its chart.

---

### Chart Page

1. Click **Chart** in the left sidebar, or click any stock symbol from the Dashboard or Market Watch.
2. Use the **symbol selector button** (top-left, shows current symbol and dropdown arrow) to search for and switch to any NEPSE-listed security.
3. Select a **timeframe** from the toolbar: 1m, 5m, 15m, 1h, 4h, 1D, 1W, or 1M.
4. Click **Indicators** to add a technical indicator overlay:
   - **SMA** — Simple Moving Average (default: period 9, yellow)
   - **EMA** — Exponential Moving Average (default: period 21, pink)
   - **RSI** — Relative Strength Index (default: period 14, shown in sub-panel)
   - **MACD** — MACD + Signal + Histogram (shown in sub-panel)
5. Hover over any candle to see its **OHLC values** in the legend at the top of the chart.
6. Click any **active indicator badge** (shown over the chart) to edit its parameters (period, color) or remove it.
7. Use the **drawing tools** in the left toolbar to add trendlines, horizontal lines, or vertical lines.

---

### Market Watch

1. Click **Market Watch** in the sidebar to see all currently traded NEPSE scrips.
2. Use the **search bar** to filter by symbol name or company name.
3. Click any **column header** (Symbol, LTP, % Chg, Qty) to sort the table ascending or descending.
4. Click any symbol to go to its chart.

---

### Watchlist

1. Click **Watchlist** in the sidebar.
2. Use the **"Add stock to watchlist..."** search bar at the top to find and add any NEPSE security. Type a symbol or company name and click the result.
3. Each watchlist card shows the stock symbol, its current Last Traded Price, and percentage change. Prices auto-refresh every 30 seconds.
4. Click the **trash icon** on any card to remove it from your watchlist.
5. Click a stock symbol card to navigate to its chart.

---

### Portfolio

1. Click **Portfolio** in the sidebar.
2. Your current **virtual cash balance** is displayed at the top.
3. Use the **stock search bar** to find a security. Click a result to open the **Trade Form**.
4. In the Trade Form: enter the **quantity** of shares and the **price per share**, then select **BUY** or **SELL**.
5. Before confirming, the system shows a full **charge breakdown**: broker commission, SEBON fee, DP charge (on sells), and capital gains tax (on profitable sells).
6. Click **Execute Trade** to confirm. Your cash balance and holdings update immediately.
7. The **Holdings** table shows your current positions: symbol, quantity, average buy price, and total invested.
8. The **Transaction History** section shows all your past buy and sell transactions in chronological order.

---

### Profile

1. Click **Profile** in the sidebar.
2. Edit your **name, email address, mobile number**, and **bio**, then click **Save Changes**.
3. To change your password, fill in **Current Password** and **New Password** (minimum 6 characters) and click **Update Password**.
4. Click **Logout** in the sidebar to end your session.

---

# CHAPTER 7: CONCLUSIONS

## 7.1 Conclusion

NEPSE Pro successfully fulfills all stated objectives as a unified, full-stack web application for Nepal Stock Exchange market analysis and portfolio simulation. The application integrates live NEPSE market data, professional-grade interactive candlestick charting with multiple technical indicators, a personalized watchlist, and a portfolio simulator with Nepal-accurate transaction charge calculations — all in a single, publicly deployed web platform.

The project demonstrates that it is feasible to build a professional-grade, domain-specific financial tool for an emerging market like Nepal using entirely free and open-source technologies — React, Express.js, TypeScript, SQLite, Tailwind CSS, and the open-source NEPSE API library — without any licensing cost.

The charge calculation engine — implementing the exact SEBON 5-tier brokerage commission structure, SEBON regulatory fee, DP charge, and capital gains tax with correct holding-period distinction — provides genuine, quantifiable value to Nepali investors beyond what any existing free platform offers. By making these costs explicit and transparent in a trade preview before execution, the system educates users about the true cost and net return of every NEPSE transaction.

The successful deployment on Vercel and Render, and the bug identification and resolution through beta testing, confirm that the system is production-ready and publicly accessible.

### 7.1.1 Significance of the System

- **Financial Literacy:** Enables Nepali investors to practice trading strategy and understand the real cost of transactions — brokerage, regulatory fees, and capital gains tax — without risking real money, using a virtual cash balance.

- **Market Accessibility:** Democratizes access to professional candlestick charting tools (previously available for NEPSE data only through expensive global platforms) for Nepali retail investors at zero cost.

- **Regulatory Compliance Awareness:** By calculating and displaying SEBON fees, broker commissions, DP charges, and CGT explicitly for every simulated trade, the system educates users about their legal tax and fee obligations.

- **Technical Foundation:** Provides a complete, open-source full-stack reference implementation for other developers building NEPSE-related tools in Nepal, covering API integration, charge calculation, FIFO portfolio logic, and dual authentication.

- **Academic Achievement:** The project covers full-stack web development, database design, REST API design, OAuth integration, financial algorithm implementation, and cloud deployment — representing a comprehensive demonstration of BCA-level computer application skills [10].

---

## 7.2 Limitations of the System

1. **No Real Trade Execution:** NEPSE Pro is a simulation platform only. Users cannot place actual buy or sell orders through any licensed NEPSE broker or TMS. Real trades must still be placed through an authorized brokerage.

2. **Third-Party NEPSE API Dependency:** All market data depends entirely on the `@rumess/nepse-api` library, which is an unofficial, community-maintained wrapper. If the upstream data source changes its structure, rate-limits access, or becomes unavailable, NEPSE Pro's market data display will be affected.

3. **SQLite Scalability:** SQLite is appropriate for a single-server deployment with a moderate number of concurrent users. It does not support horizontal scaling or high-concurrency simultaneous write operations required for a large production user base.

4. **No WebSocket Real-Time Push:** The current implementation uses polling (5-second interval for chart updates, 30-second interval for watchlist prices). A true WebSocket-based real-time data push would reduce latency and eliminate unnecessary polling calls when data has not changed.

5. **In-Memory Cache Volatility:** The API response cache is held in the Node.js process memory. A server restart (common on Render's free tier due to sleep/wake cycles) clears all cached data, causing a brief period where all requests hit the external NEPSE API until the cache is repopulated.

6. **No Fundamental Analysis Data:** The platform provides only technical/price data. Company fundamentals (EPS, P/E ratio, book value, annual dividend, promoter holding percentage) are not currently integrated.

7. **No Price Alerts:** The watchlist tracks live prices but does not support configurable price alert thresholds or push notifications when a target price is reached.

8. **Limited Historical Depth:** The depth of historical OHLCV data available depends on what the NEPSE API source exposes. Very long-term historical analysis (5+ years) may not be available for all securities.

---

## 7.3 Future Scope of the Project

The following enhancements are identified as high-value directions for future development:

1. **WebSocket Real-Time Data Feed:** Replace the current polling mechanism with a WebSocket server (using `socket.io` or native WebSockets) to push live NEPSE index and price updates to all connected clients simultaneously, reducing latency and server load.

2. **Price Alert System:** Allow users to set a target price threshold for any watchlist security and receive a notification (email or browser push notification via the Web Push API) when the stock crosses that price.

3. **Company Fundamental Data Integration:** Integrate financial data from NEPSE/SEBON public disclosures (EPS, P/E ratio, book value, dividend history, quarterly reports) to support fundamental analysis alongside the existing technical analysis tools.

4. **Advanced Portfolio Analytics:** Add metrics such as sector allocation breakdown, overall portfolio beta against the NEPSE index, Sharpe ratio, maximum drawdown, and comparison of portfolio return versus the NEPSE index return over the same holding period.

5. **Real Portfolio Import:** Allow users to import their actual NEPSE transaction history from a broker TMS or CSV file, enabling them to track their real portfolio alongside the virtual simulation.

6. **News and Announcements Feed:** Integrate a NEPSE-related news feed, company announcements, AGM notices, and SEBON circulars from public sources directly into the dashboard.

7. **PostgreSQL Migration:** Migrate from SQLite to PostgreSQL to support horizontal scaling, concurrent write operations, and production-grade reliability for a larger user base.

8. **Mobile Native Application:** Develop a React Native (Expo) mobile application sharing the same Express.js backend API, providing a native iOS and Android experience with push notifications.

9. **Paper Trading Competitions:** Implement a leaderboard-based paper trading competition feature where multiple users compete with the same starting virtual balance over a defined period (e.g., one month), ranked by final portfolio return.

10. **AI-Powered Market Insights:** Leverage the Google Gemini API (the `@google/generative-ai` SDK is already installed in the backend) to provide natural language summaries of individual stock performance, plain-English explanations of technical indicator signals, and AI-generated market commentary for the NEPSE index.

---

# REFERENCES

[1] Nepal Stock Exchange (NEPSE), "Official NEPSE Website," [Online]. Available: https://nepalstock.com. [Accessed: May–June 2025].

[2] R. Magar, "NEPSE API," GitHub Repository, 2023. [Online]. Available: https://github.com/rumess/nepse-api. [Accessed: May–June 2025].

[3] Meta Platforms, Inc., "React – The Library for Web and Native User Interfaces," [Online]. Available: https://react.dev. [Accessed: May 2025].

[4] OpenJS Foundation, "Express – Fast, Unopinionated, Minimalist Web Framework for Node.js," [Online]. Available: https://expressjs.com. [Accessed: May 2025].

[5] Tailwind Labs, Inc., "Tailwind CSS – A Utility-First CSS Framework," [Online]. Available: https://tailwindcss.com. [Accessed: May 2025].

[6] TradingView, Inc., "Lightweight Charts Documentation," [Online]. Available: https://tradingview.github.io/lightweight-charts/. [Accessed: May 2025].

[7] Auth0 by Okta, "JSON Web Token (JWT) Introduction," [Online]. Available: https://jwt.io/introduction. [Accessed: May 2025].

[8] Vercel, Inc., "Vercel – Develop, Preview, Ship," [Online]. Available: https://vercel.com. [Accessed: May 2025].

[9] Nodemailer, "Nodemailer – Node.js Email Sending Library," [Online]. Available: https://nodemailer.com. [Accessed: May 2025].

[10] I. Sommerville, *Software Engineering*, 10th ed. Pearson, 2015.

[11] Figma, Inc., "Figma – The Collaborative Interface Design Tool," [Online]. Available: https://www.figma.com. [Accessed: May 2025].

[12] S. Almarri and P. Gardiner, "Portfolio management framework for public sector projects using a strategic approach," *Procedia – Social and Behavioral Sciences*, vol. 119, pp. 229–236, 2014. doi: 10.1016/j.sbspro.2014.03.027.

[13] H. R. Varian, "Big data: New tricks for econometrics," *Journal of Economic Perspectives*, vol. 28, no. 2, pp. 3–28, 2014. doi: 10.1257/jep.28.2.3.

[14] Mero Lagani, "Merolagani Official Website," [Online]. Available: https://www.merolagani.com. [Accessed: May 2025].

[15] ShareSansar, "ShareSansar Official Website," [Online]. Available: https://www.sharesansar.com. [Accessed: May 2025].

---

*End of Report*

---

> **Note on Diagrams:** All figures marked with *(Insert figure here)* require you to draw the diagram in a tool such as draw.io (diagrams.net), Lucidchart, StarUML, or Microsoft Visio, then paste or embed the image at that position in your final Word/PDF document. The design specification text below each figure placeholder describes exactly what the diagram must contain — treat it as a drawing specification, not as text to include in the final document.
