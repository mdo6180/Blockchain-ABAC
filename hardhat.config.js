/** @type import('hardhat/config').HardhatUserConfig */
require('dotenv').config();
require("@nomiclabs/hardhat-ethers");

const { API_URL, PRIVATE_KEY_1, MUMBAI_API_URL } = process.env;

module.exports = {
   solidity: "0.8.17",
   defaultNetwork: "goerli",
   networks: {
      hardhat: {},
      goerli: {
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY_1}`]
      },
      mumbai: {
        url: MUMBAI_API_URL,
        accounts: [`0x${PRIVATE_KEY_1}`, `0x${PRIVATE_KEY_2}`]
      }
   },
}
