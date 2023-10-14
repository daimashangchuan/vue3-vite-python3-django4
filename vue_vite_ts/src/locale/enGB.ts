const locale = {

  common: {
    safeAndReliable: "Safe Reliable",
    strongAndStable: "Strong Stable",
    quantitativePlatform: "Quantitative",
    desc: "Professional Technology, Transparent Data, Freedom and Efficiency, Scientific Wealth Management",

    nothingMore: "It is all, nothing more！"
  },


  auth: {

    login: 'Login',
    signUp: 'Sign Up',
    forget: 'Forgot password',

    username: {
      label: 'Username',
      placeholder: 'Please enter your username, at least 6 characters!',
      message: 'Please enter a valid username, at least 6 characters!',
    },
    email: {
      label: 'Email',
      placeholder: 'Please enter your email!',
      message: 'Please enter a valid email!',
    },
    verifyCode: {
      label: 'Email Verification Code',
      placeholder: 'Please enter a 2-digit verification code!',
      message: 'Please enter a valid 2-digit verification code!',
    },
    password: {
      label: 'Password',
      placeholder: 'Please enter your password, at least 6 characters!',
      message: 'Please enter a valid password, at least 6 characters!',
    },
    passwordConfirm: {
      label: 'Confirm Password',
      placeholder: 'Password Confirmation',
      message: 'The confirmation password does not match the password!',
    },

    sendAgain: 'again',
    send: 'Send',

    read: 'I have read',
    agreement: 'the User Agreement',
    checkAgreement: 'Please check "I have read the User Agreement"!',

    loginAccount: "Don't have an account yet?",
    loginNow: 'Sign Up Now',

    signUpAccount: 'Already have an account?',
    signUpNow: 'Login Now',

    confirm: 'Confirm',
  },


  header: {
    list: [
      { label: 'Market', key: '/market', id: 1 },
      { label: 'Strategy', key: '/strategy', id: 2 },
      { label: 'Ranking', key: '/ranking', id: 3 },
      { label: 'Team', key: '/team', id: 4 },
      { label: 'Transaction', key: '/transaction', id: 5 },
      { label: 'Electronic Bill', key: '/bill', id: 6 },
      { label: 'Accumulated Profit', key: '/profit', id: 7 },
      { label: 'API Authorization', key: '/apiauth', id: 8 },
    ],
    lang: [
      { label: "Chinese", key: 'zh' },
      { label: "English", key: 'en' },
      { label: "Japanese", key: 'ja' },
    ],
    auth: {
      login: 'log in',
      signUp: 'Sign up',
      signOut: 'Sign out'
    },
  },


  footer: {
    content: 'Options trading entails significant risk and is not appropriate for all customers. Options transactions are often complex and may involve the potential of losing the entire investment in a relatively short period of time. Certain complex options strategies carry additional risk, including the potential for losses that may exceed the original investment amount.',
    copyright: 'All rights reserved',
  },


  market: {
    notice: 'Announcement',
    more: 'View More',
    moreNews: 'View More News',

    informationLang: {
      information: 'News and Information',
    },

    marketLang: {
      market: "Market",
      name: "Name",
      turnover: "Turnover(USDT)",
      price: "Latest Price",
      change: "24H Change",
      trade: "Go to Trade",
    },

    functionsLang: {
      functions: "Common Functions",

      trust: 'Trust Trading',
      transaction: 'API Trading',
      service: 'Service Selection',
      promotion: 'Invite & Commission',
    },

    partnersLang: {
      partners: 'Partners'
    },
  },


  ranking: {
    ranking: 'Ranking',
    rankingTabList: [
      { value: 1, label: 'Weekly Profit', icon: 'MoneyCollectOutlined' },
      { value: 2, label: 'Weekly ROI', icon: 'StockOutlined' },
      { value: 3, label: 'Monthly Profit', icon: 'PayCircleOutlined' },
      { value: 4, label: 'Monthly ROI', icon: 'BarChartOutlined' },
      { value: 5, label: 'Total Profit', icon: 'AccountBookOutlined' },
      { value: 6, label: 'Total ROI', icon: 'FundOutlined' },
      { value: 7, label: 'Total Assets', icon: 'AuditOutlined' },
    ],
    income: "Pnl",
    rate: "ROI"
  },


  strategy: {
    strategy: "Quantitative Strategies",
    strategyList: [
      {
        name: 'A01 Low Risk Low Return',
        rate: '50%-100%',
        color: "var(--c-main-10)",
        tagColor: "var(--c-main-80)",
        desc: [
          'Customer Profit: 20%-50% · Annual Management Fee: 2%',
          'Free Management Fee: VIP3 (1 million USD) · Leverage: 0-5',
          'Our Share: 70%'
        ],
        content: [
          'Trading Method: API · Dividend Period: Quarterly · Protocol Period: Four quarters',
          'Tradable Assets: Stablecoins/ETH/BTC'
        ]
      },
      {
        name: 'B01 Medium Risk Medium Return',
        rate: '100%-300%',
        color: "var(--c-main-30)",
        tagColor: "var(--c-main-90)",
        desc: [
          'Customer Profit: 50%-150% · Annual Management Fee: 2%',
          'Free Management Fee: VIP3 (1 million USD) · Leverage: 0-5',
          'Our Share: 60%'
        ],
        content: [
          'Trading Method: API · Dividend Period: Quarterly · Protocol Period: Four quarters',
          'Tradable Assets: Stablecoins/ETH/BTC'
        ]
      },
      {
        name: 'C01 High Risk High Return',
        rate: '300%-600%',
        color: "var(--c-main-40)",
        tagColor: "var(--c-main-100)",
        desc: [
          'Customer Profit: 150%+ · Annual Management Fee: 2%',
          'Free Management Fee: VIP3 (1 million USD) · Leverage: 5-20',
          'Our Share: 50%'
        ],
        content: [
          'Trading Method: API · Dividend Period: Quarterly · Protocol Period: Four quarters',
          'Tradable Assets: Stablecoins/ETH/BTC'
        ]
      }
    ],
  },

}


export default locale;





