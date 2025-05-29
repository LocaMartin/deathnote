<div align="center">
  <img align="center" style="height: 250px; width: 250px;" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnJnejUybnhlMzZ6cWJ4OGo2cHNveTAzZHppYjF1cWw4aThnaGhxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/rpIPFqrxkXTShsBhBS/giphy.gif">
</div>

<p align="center"><i><b>Crypto</b></i></p>

<hr>

> This document probably covers everything you need to know to start crypto/smart contract based bug bounty or devlopment.

<hr>

<details>
  <summary><b>Table of Content</b></summary>

- [1. What is Crypto?](#what-is-crypto)


- [2. Hyistory & origin of Crypto]()
  - Pre-Bitcoin Concepts:
    - DigiCash 
    - HashCash 
    - Cypherpunk Movement
  - Bitcoin Whitepaper (2008):
    - Satoshi Nakamoto’s Vision
  - Key Milestones:
     - Mt. Gox Hack (2014)
     - Ethereum Launch (2015)
     - DAO Hack (2016)
     - Ethereum’s Merge (2022)
     - Bitcoin ETFs (2024)
  - Evolution of Blockchain:
     - From Currency to Smart Contracts

- [3. How crypto works ?]()
   - Layers of crypto ecosystem
   - What is Blockchain 
   - Blockchain Fundamentals:
     - Distributed Ledger
     - Immutability
   - Consensus Mechanisms: 
       - PoW 
       - PoS 
       - DPoS 
       - PoA
    - Core Principles:
       - Decentralization
       - Transparency
       - Trustlessness
    - Blockchain Layers:
       - Layer 0 (Polkadot, Cosmos)
       - Layer 1 (Bitcoin, Ethereum, Solana)
       - Layer 2 (Optimism, zkSync, Lightning Network) 
    - Cryptography:
       - Hashing 
          - SHA-256
          - KECCAK-256
       - Digital Signatures & Public-Key Cryptography
       - Zero-Knowledge Proofs 
         -  zk-SNARKs
         -  zk-STARKs
    -  Interoperability:
         - Cross-Chain Bridges
         - Cosmos IBC
         - Polkadot Parachains

- [4. Types of crypto.]()
   - Coins
   - Tokens
   - Currency Tokens: Bitcoin (BTC), Monero (XMR)
   - Utility Tokens: Ethereum (ETH), Chainlink (LINK)
   - Security Tokens: Tokenized Assets (RealT, tZERO)
   - Stablecoins: USDC (Collateralized), DAI (Algorithmic)
   - Memecoins: Dogecoin (DOGE), Shiba Inu (SHIB)
   - CBDCs: Digital Yuan, e-Euro, Project Sand Dollar
   - Governance Tokens: UNI (Uniswap), AAVE
 
- [5. Crypto company and their services]()
   - Exchanges:
     - Centralized (Binance, Coinbase) vs. Decentralized (Uniswap)
   - Custody Solutions: Fireblocks, Coinbase Custody
   - Insurance: Nexus Mutual, Etherisc
   - Analytics & Compliance: 
     - Chainalysis
     - TRM Labs
   - Institutional Adoption:
     - BlackRock’s Bitcoin ETF
     - Fidelity Custody

- [6. Smart Contracts & Crypto Development]()  
   - Common Crypto Infrastructures
     -  Ethereum Infrastructure
        - Execution Clients: 
          - Geth (Go)
          - Nethermind (C#)
          - Besu (Java)
        - Consensus Clients: 
          - Lighthouse (Rust)
          - Prysm (Go)
        - Node Services:
          - RPC Endpoints
          - Peer Discovery (Kademlia)
          - enode Protocol    
 
   - What is smart contract ?
     - Code-as-Law
     - Automation
     - ERC Standards (ERC-20, ERC-721)
   - Development Ecosystem:
     - Languages: Solidity, Vyper, Rust (Solana), Move (Aptos)
     - Frameworks: Hardhat, Truffle, Foundry
     - IDEs: Remix, VS Code Extensions
   - dApps (Decentralized Applications):
     - DeFi (Aave, Compound), Gaming (Axie Infinity), Social (Lens)
     - solidity programing
 
- [7. Test,bug bounty and hacking]()
   - cryto bug bouty platforms
   - vulnersbility ( case study )
     - Reentrancy 
     - Oracle Manipulation
     - Frontrunning
     - Flash Loan Exploits
   - Tools
     - known tools
       - foundry
         - cast
         - forge
         - anvil
         - chisel
       - Slither
       - MythX
       - Certora (Formal Verification)
     - personal tool
       - cryptocut
   - Testing/attack vector & Payload
      - dApp
      - web
        - Header Injection
        - XSS
        - SQLi
        - OS ( linux/bash )
   - Ethereum clients 
      - reth
      - geth   
   - Language
     - server language
         - Go lang , Python , .NET
     - Etherium client language
         - (reth)rust , geth( Go lang )
     - Solidity
       - sol         
   - Service or protocol ( that run on  inside node )
        - enode
        - dict
   - Incident Response
   - Whitehat Hacks
   - Fund Freezing
   - Post-Mortem Analysis
   - Crypto Hacking attacks that shocked the world ( case study )
     - Attack Types:
       - 51% Attacks, Rug Pulls, Phishing, MEV Exploits
     - Case Studies:
        - Poly Network Hack (611M),RoninBridgeExploit(611M),RoninBridgeExploit(625M)
     - Defense Mechanisms:
        - Multi-Sig Wallets, Time Locks, Decentralized Oracles (Chainlink)

- [8. Use of bot in Crypto]()
  - MEV Bots: 
     - Arbitrage
     - Sandwich Attacks
  - Trading Bots: 
     - Grid Trading
     - Sniper Bots
  - Liquidity Sniping: 
     - Uniswap LP Exploitation
- [9. Crypto mining]()
  - PoW Mining: 
     - ASICs vs. GPUs
     - Mining Pools (AntPool)
  - Environmental Impact: 
     - Energy Debates
     - Green Mining Initiatives
  - Cloud Mining: 
     - Pros/Cons
     - Hashrate Marketplaces

- [10. Ai in crypto]()
 
- [11. Privacy & Anonymity]()
  - Privacy Coins: 
     - Monero (Ring Signatures)
    - Zcash (zk-SNARKs)
  - Privacy Tools: 
     - Tornado Cash
     - Aztec Protocol

- [12. Regulation & Compliance]()
  - Global Frameworks:
     -  MiCA (EU)
     -  FATF Travel Rule
  - SEC Actions: 
     - Ripple Lawsuit
     - Security Token Classification
  - AML/KYC: 
     - On-Chain Analytics (Elliptic)
     - TRM Labs

- [13. Tokenomics & Economic Design]()
  - Supply Mechanics: 
     - Fixed (BTC) vs. Inflationary (ETH)
  - Burns: 
     - BNB Auto-Burn
     - SHIB Token Burns
  - Vesting Schedules: 
     - Team/Investor Lockups (e.g., Solana)

- [14. Decentralized Governance (DAOs)]()
  - Governance Models:
     - Token-Based (UNI)
     - Reputation-Based (MakerDAO)
  - Tools: 
     - Snapshot (Off-Chain Voting) 
     - Aragon, Tally

- [15. Scalability Solutions]()
  - Rollups: 
     - Optimistic (Arbitrum) vs. ZK (zkSync, StarkNet)
  - Sharding: 
     - Ethereum 2.0
     - Near Protocol
  - Sidechains: 
     - Polygon
     - SKALE

- [16. Ethics & Criticisms]()
  - Scams:
     - Ponzi Schemes (OneCoin)
     - Fake ICOs
  - Energy Use: 
     - Bitcoin’s Carbon Footprint
     - PoS Transition
  - Wealth Inequality:
     - Early Adopter Concentration

- [17. Real-World Use Cases]()
  - Supply Chain: 
     - VeChain
     - IBM Food Trust
  - Healthcare: 
     - MediBloc
     - Patientory
  - Voting: 
     - Voatz 
     - Decentralized Governance (ENS DAO)

- [18. Web3 & Metaverse]()
  - NFTs: 
     - Digital Art (OpenSea)
     - Gaming (STEPN)
  - Virtual Land: 
     - Decentraland
     - The Sandbox
  - Identity: 
     - Soulbound Tokens (SBTs)
     - ENS Domains

- [19. Appendices]()
  - Glossary: 
     - Gas
     - Wallet
     - Hard Fork
     - AMM
     - MEV
  - Resources:
  - Explorers: 
     - Etherscan
     - Solscan
  - Learning: 
     - CryptoZombies
     - Ethereum.org
     - CoinGecko
  - Case Studies:
     - FTX Collapse
     - Terra-Luna Crash

</details>

<hr>



<hr>

<!--
## What is Crypto?
*Content goes here...*

## History & Origin of Crypto
*Content goes here...*

## How Crypto Works?
*Content goes here...*

### Layers of the Crypto Ecosystem
*Content goes here...*

## Types of Crypto
*Content goes here...*

<details>
  <summary>List of crypto coins</summary>
- Well-Known crypto (Major, Altcoin & Token, and Beyond the Popular).
<br> 
[hdsgkjhdg](./tables/crypto_coin.md)
<br>
- List of all coins and its real time stats
<iframe src="https://coinmarketcap.com/all/views/all/" width="100%" height="800" frameborder="0"></iframe>
</details>

## Crypto Companies and Their Services
*Content goes here...*

## What is a Smart Contract?
*Content goes here...*

## Development

### dApps
*Content goes here...*

### Solidity Programming
*Content goes here...*

## Testing, Bug Bounty, and Hacking
*Content goes here...*

### Vulnerability Explanation (Case Study)
*Content goes here...*

### Tools

#### Known Tools – Foundry
- **Cast**
- **Forge**
- **Anvil**
- **Chisel**

#### Personal Tools
- **Cryptocut**

### Testing Vectors & Payload

#### dApp
*Content goes here...*

#### Web
- **Header Injection**
- **XSS**
- **SQLi**
- **OS (Linux/Bash)**

## Ethereum Clients
- **reth**
- **geth**

## Language

### Server Language
- **Go**, **Python**, **.NET**

### Ethereum Client Language
- **reth:** Rust  
- **geth:** Go

### Services/Protocols (That Run Inside a Node)
- **enode**
- **dict**

## Crypto Hacking Attacks
*Content goes here...*

## Use of Bots in Crypto
*Content goes here...*

## Crypto Mining
*Content goes here...*


1. The Blockchain (Crypto Layer)

   - Crypto: At its foundation, "crypto" refers to cryptocurrencies and blockchain technology. This includes networks like Ethereum and Bitcoin where digital assets are secured by cryptography. In these ecosystems, all activities—from transactions to executing contracts—occur on a decentralized blockchain.

   - Smart Contract: A smart contract is a piece of code written (often in  Solidity for Ethereum) that runs on a blockchain. These contracts are self-executing and manage everything from token transfers to complex financial instruments. They’re deployed on the blockchain and, once live, are immutable and maintained across all nodes.

2. The Application Layer

    - dApp (Decentralized Application): A decentralized application is built on top of the blockchain using smart contracts as its backend logic. While the dApp itself might have a user interface (typically run in a browser or mobile environment), its core operations interact with smart contracts on the blockchain. Think of the dApp as the front-facing application that users engage with, which indirectly triggers smart contracts on the blockchain.

    - web3: Often, “web3” refers to the new paradigm of the decentralized web. More technically, libraries like [Web3.js]("https://web3js.readthedocs.io/en/v1.10.0/") (or [ethers.js](https://docs.ethers.org/v5/)) are JavaScript interfaces that allow dApps to interact with blockchain networks. These libraries send commands (such as reading data or executing transactions) to blockchain nodes using standard protocols like JSON-RPC.

3. The Node Layer

    - Linux Node: A node is any computer that participates in the blockchain network by running client software. Many of these nodes run on Linux due to its stability and performance in network environments. These nodes are responsible for validating and relaying transactions and for running smart contracts as part of the decentralized blockchain network.

    - Geth (Go Ethereum) & Reth:

        - Geth: This is the official Go implementation of the Ethereum client. It runs on nodes (often on Linux) and exposes a JSON-RPC interface which allows external applications to interact with the Ethereum network.

        - Reth: This is a newer Ethereum client developed in Rust. It provides similar functionalities to Geth, including exposing JSON-RPC endpoints, but is built with a different programming language focused on performance and safety.

    Go RPC Server: In the context of blockchain nodes, when you hear about a Go RPC server, it typically refers to the JSON-RPC server component embedded in clients like Geth. This server listens for JSON-RPC requests (coming from libraries like Web3.js) and processes them to interact with the blockchain (e.g., submitting transactions, querying blockchain state).

**Visualizing the Ecosystem**

```js
        [ dApp Frontend ]
               │
       (web3.js / ethers.js)
               │
      JSON-RPC Communication
               │
 [ Linux Node Running Geth/Reth (RPC Server)]
               │
       Ethereum Blockchain Network
               │
     [Smart Contracts Deployed]

```

- Users interact with the dApp, which uses Web3 libraries to send JSON-RPC calls.

- These calls hit a node (running on Linux) that’s powered by Geth or Reth.

- The node processes these JSON-RPC requests and communicates with the blockchain where smart contracts reside.

Summury:

- Crypto and Blockchain: The underlying network and digital currency (e.g., Ethereum, Bitcoin) that provide the decentralized infrastructure.

- Smart Contracts: Code deployed on the blockchain to execute predefined rules.

- dApps: Applications that users interact with; they leverage smart contracts for backend operations.

- web3 & JSON-RPC: The bridge between dApps and blockchain nodes, with JSON-RPC being the protocol used to send commands, and web3 libraries serving as an abstraction layer.

- Linux Nodes running Geth/Reth: The actual servers that validate blockchain activities and offer JSON-RPC endpoints for communication.

This layered structure explains why the ecosystem may appear confusing at first—the terms refer to different parts of a broader system, each responsible for a specific role in enabling decentralized applications.

**Additional Concepts**

- Consensus Mechanisms: Understand how blockchain networks achieve agreement on the state of the ledger. For Ethereum, this is currently Proof of Stake (PoS), while Bitcoin uses Proof of Work (PoW). Knowing how these work can illuminate attack surfaces or scalability challenges.

- Layer 2 Solutions: Platforms like Polygon (mentioned earlier) are designed to improve scalability and reduce transaction costs for blockchains. These are vital for dApps that require high throughput but may introduce unique vulnerabilities or integration challenges.

- Token Standards (ERC-20, ERC-721, etc.): Recognizing the key Ethereum standards for tokens (ERC-20 for fungible tokens and ERC-721 for NFTs) can help you understand how smart contracts interact with assets. For bug bounty purposes, token-related vulnerabilities (e.g., minting issues) are worth exploring.

- Gas Optimization: On Ethereum, every transaction involves “gas” fees. Inefficient smart contracts can lead to excessive fees. Exploring optimization techniques can help identify flaws in contract design that lead to wasted resources.

- Governance and DAOs: Many smart contracts enable decentralized governance. By studying how voting, proposal management, and fund allocation work in DAOs (Decentralized Autonomous Organizations), you can identify opportunities for manipulation or abuse.

- Cross-Chain Interoperability: With the rise of multi-chain ecosystems (e.g., using bridges between Ethereum and Binance Smart Chain), there are vulnerabilities tied to cross-chain communication and token transfers. These are often exploited, making them lucrative for bounty hunters.

- Off-Chain Computation: While smart contracts execute on-chain, some computations (e.g., complex calculations or external data fetching) are performed off-chain using tools like Layer 2 Rollups or zk-SNARKs. Issues related to these interactions can open attack opportunities.

- Advanced RPC Protocols: Beyond JSON-RPC, explore how WebSocket connections handle real-time updates (subscriptions) and investigate potential edge cases. Techniques like fuzzing subscription methods might reveal interesting weaknesses.

- MEV (Maximal Extractable Value): MEV refers to the additional value blockchain validators can extract by reordering transactions. This has implications for front-running and economic vulnerabilities in DeFi.

Summery:

The blockchain ecosystem can be conceptually divided into several layers that define the technology stack and processes. Here's a breakdown:
1. Layer 0: Underlying Infrastructure

    - Description: This layer supports the physical infrastructure and protocols that underpin blockchains.

    - Components:

        - Networking protocols (e.g., TCP/IP, P2P protocols for node communication).

        Hardware like servers, data centers, and individual nodes (Linux systems running Geth or Reth).

        Consensus algorithms (e.g., Proof of Stake, Proof of Work).

2. Layer 1: Base Blockchain Protocol

    - Description: This is the core blockchain network where transactions and smart contracts are processed.

    - Components:

        Blockchains like Ethereum, Bitcoin, Solana.

        Smart contract execution (e.g., EVM for Ethereum).

        Native cryptocurrencies (e.g., ETH for Ethereum, BTC for Bitcoin).

3. Layer 2: Scalability and Off-Chain Solutions

    - Description: These are solutions designed to enhance blockchain scalability and reduce transaction costs.

    - Components:

        - Layer 2 protocols like Polygon, Arbitrum, and Optimism.

        - Techniques like Rollups (zk-Rollups, Optimistic Rollups) and payment channels (e.g., Lightning Network).

        - Off-chain computations and temporary state storage.

4. Layer 3: Application Layer

    - Description: This is where decentralized applications (dApps) live, enabling user interaction with blockchain systems.

    - Components:

        - dApps (e.g., Uniswap, Aave, OpenSea).

        - Web3 libraries (e.g., Web3.js, ethers.js) for blockchain interaction.

        - User interfaces for trading, gaming, governance, etc.

5. Layer 4: User Interaction Layer

    - Description: The front-facing layer that provides access to blockchain functionalities and services.

    - Components:

        - Crypto wallets (e.g., MetaMask, Trust Wallet) enabling users to sign transactions.

        - APIs and SDKs for developers to integrate blockchain into traditional platforms.

        - Browser extensions and mobile applications providing seamless blockchain access.

**Optional Additional Layers**

   - Cross-Chain Layer (Bridges): Facilitates interoperability between different blockchains, enabling token and data transfer across networks (e.g., Wormhole, Polkadot's relay chains).

   - Governance Layer: Refers to decentralized decision-making systems (e.g., DAOs) that manage updates, funding, and community rules.

   - Security Layer: Encompasses monitoring, audits, and mechanisms (like slashing in Proof of Stake) to maintain network integrity and prevent malicious activities.

Each layer plays a unique role in building the decentralized ecosystem, ensuring seamless functionality, scalability, and usability. Depending on your focus—whether it’s smart contracts, infrastructure, or dApp security—you’ll want to dive deeper into specific layers.
-->