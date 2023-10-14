
const locale = {

  common: {
    safeAndReliable: "安全可靠",
    strongAndStable: "强大稳定",
    quantitativePlatform: "量化平台",
    desc: "专业技术、数据透明、自由高效、科学理财",

    nothingMore: "已经到底了，没有更多了！"
  },


  auth: {

    login: '登录',
    signUp: '注册',
    forget: '忘记密码',

    username: {
      label: '用户名',
      placeholder: '请输入用户名，至少2个字符！',
      message: '请输入正确的用户名，至少2个字符！'
    },
    email: {
      label: '邮箱',
      placeholder: '请输入邮箱！',
      message: '请输入正确的邮箱！'
    },
    verifyCode: {
      label: '邮箱验证码',
      placeholder: '请输入6位数字验证码！',
      message: '请输入正确的6位数字验证码！'
    },
    password: {
      label: '密码',
      placeholder: '请输入密码，最少6个字符！',
      message: '请输入正确的密码，最少6个字符！',
    },
    passwordConfirm: {
      label: '确认密码',
      placeholder: '密码确认',
      message: '您输入的确认密码与密码不匹配！',
    },

    sendAgain: '秒 再次发送',
    send: '发送',

    read: '我已阅读',
    agreement: '《用户协议》',
    checkAgreement: "请勾选我已阅读用户协议！",

    loginAccount: '还没有帐号',
    loginNow: '立即注册',

    signUpAccount: '已有帐号',
    signUpNow: '立即登录',

    confirm: '确认',

  },


  header: {
    list: [
      { label: '行情', key: '/market', id: 1 },
      { label: '策略', key: '/strategy', id: 2 },
      { label: '排行榜', key: '/ranking', id: 3 },
      { label: '我的团队', key: '/team', id: 4 },
      { label: '交易记录', key: '/transaction', id: 5 },
      { label: '电子账单', key: '/bill', id: 6 },
      { label: '累计盈利', key: '/profit', id: 7 },
      { label: 'API授权', key: '/apiauth', id: 8 },
    ],
    lang: [
      { label: "中文", key: 'zh', },
      { label: "英文", key: 'en', },
      { label: "日文", key: 'ja', },
    ],
    auth: {
      login: '登录',
      signUp: '注册',
      signOut: '退出'
    }
  },


  footer: {
    content: '期权交易存在重大风险，并不适合所有客户。期权交易通常很复杂，并且可能涉及在相对较短的时间内损失全部投资的可能性。某些复杂的期权策略带有额外的风险，包括可能超过原始投资金额的潜在损失。',
    copyright: '版权所有'
  },


  market: {

    notice: '公告',
    more: '查看更多',
    moreNews: '查看更多新闻',


    informationLang: {
      information: '新闻资讯',
    },


    marketLang: {
      market: "行情",
      name: "名称",
      turnover: "成交量(USDT)",
      price: "最新价",
      change: "24H涨幅",
      trade: "去交易",
    },


    functionsLang: {
      functions: "常用功能",
      trust: '委托交流',
      transaction: 'API交易',
      service: '服务选择',
      promotion: '邀请返佣'
    },


    partnersLang: {
      partners: '合作伙伴',
    },
  },

  ranking: {
    ranking: '排行榜',
    rankingTabList: [
      { value: 1, label: '周收益', icon: 'MoneyCollectOutlined' },
      { value: 2, label: '周收益率', icon: 'StockOutlined' },
      { value: 3, label: '月收益', icon: 'PayCircleOutlined' },
      { value: 4, label: '月收益率', icon: 'BarChartOutlined' },
      { value: 5, label: '总收益', icon: 'AccountBookOutlined' },
      { value: 6, label: '总收益率', icon: 'FundOutlined' },
      { value: 7, label: '总资产', icon: 'AuditOutlined' },
    ],
    income: "收益",
    rate: "收益率"
  },


  strategy: {
    strategy: "量化策略",
    strategyList: [
      {
        name: 'A01低风险低收益',
        rate: '50%-100%',
        color: "var(--c-main-10)",
        tagColor: "var(--c-main-80)",
        desc: [
          '客户收益：20%-50% · 年管理费：2%',
          '免管理费：VIP3（100万USD）·杠杆倍数：0-5',
          '我方分成：70%'
        ],
        content: [
          '交易方式：API · 分成周期：季度 · 协议周期：四季度',
          '可交易资产：Stablecoins/ETH/BTC'
        ]
      },
      {
        name: 'B01中风险中收益',
        rate: '100%-300%',
        color: "var(--c-main-30)",
        tagColor: "var(--c-main-90)",
        desc: [
          '客户收益：50%-150% · 年管理费：2%',
          '免管理费：VIP3（100万USD）·杠杆倍数：0-5',
          '我方分成：60%'
        ],
        content: [
          '交易方式：API · 分成周期：季度 · 协议周期：四季度',
          '可交易资产：Stablecoins/ETH/BTC'
        ]
      },
      {
        name: 'C01高风险高收益',
        rate: '300%-600%',
        color: "var(--c-main-40)",
        tagColor: "var(--c-main-100)",
        desc: [
          '客户收益：150% + · 年管理费：2%',
          '免管理费：VIP3（100万USD）·杠杆倍数：5-20',
          '我方分成：50%'
        ],
        content: [
          '交易方式：API · 分成周期：季度 · 协议周期：四季度',
          '可交易资产：Stablecoins/ETH/BTC'
        ]
      }
    ],
  },

}


export default locale;