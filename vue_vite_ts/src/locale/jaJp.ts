const locale = {

  common: {
    safeAndReliable: "あんぜん",
    strongAndStable: "安定している",
    quantitativePlatform: "りょうか",
    desc: "専門技術、透明なデータ、自由で効率的、科学的な資産運用",

    nothingMore: "これがすべてで、他にはありません！"
  },


  auth: {

    login: 'ログイン',
    signUp: '登録',
    forget: 'パスワードを忘れる',

    username: {
      label: 'ユーザー名',
      placeholder: 'ユーザー名を入力してください。少なくとも2文字です！',
      message: '有効なユーザー名を入力してください。少なくとも2文字です！',
    },
    email: {
      label: 'メールアドレス',
      placeholder: 'メールアドレスを入力してください！',
      message: '有効なメールアドレスを入力してください！',
    },
    verifyCode: {
      label: 'メール確認コード',
      placeholder: '6桁の確認コードを入力してください！',
      message: '有効な6桁の確認コードを入力してください！',
    },
    password: {
      label: 'パスワード',
      placeholder: 'パスワードを入力してください。少なくとも6文字です！',
      message: '有効なパスワードを入力してください。少なくとも6文字です！',
    },
    passwordConfirm: {
      label: 'パスワードの確認',
      placeholder: 'パスワードの確認',
      message: '確認用のパスワードがパスワードと一致しません！',
    },
    sendAgain: '秒後に再送信',
    send: '送信',

    read: '私は読みました',
    agreement: '《ユーザー協定》',

    checkAgreement: '「ユーザー協定を読みました」にチェックしてください！',

    loginAccount: 'まだアカウントをお持ちでないですか？',
    loginNow: '今すぐ登録',

    signUpAccount: 'すでにアカウントをお持ちですか？',
    signUpNow: 'ログインする',

    confirm: '確認',
  },


  header: {
    list: [
      { label: '相場', key: '/market', id: 1 },
      { label: 'ポリシー', key: '/strategy', id: 2 },
      { label: 'ランキング', key: '/ranking', id: 3 },
      { label: '私のチーム', key: '/team', id: 4 },
      { label: 'トランザクション', key: '/transaction', id: 5 },
      { label: '電子請求書', key: '/bill', id: 6 },
      { label: '累計利益', key: '/profit', id: 7 },
      { label: 'API承認', key: '/apiauth', id: 8 },
    ],
    lang: [
      { label: "中国語", key: 'zh', },
      { label: "英語", key: 'en', },
      { label: "日本語", key: 'ja', },
    ],
    auth: {
      login: 'ログイン',
      signUp: '登記',
      signOut: 'ログアウト'
    },
  },


  footer: {
    content: 'オプション取引には重大なリスクが伴い、すべてのお客様に適しているとは限りません。オプション取引は一般的に複雑で、比較的短期間で投資額全体を失う可能性があります。一部の複雑なオプション戦略には、元本を超える損失の可能性を含む追加のリスクがあります。',
    copyright: '全著作権所有',
  },


  market: {
    notice: 'お知らせ',
    more: 'もっと見る',
    moreNews: 'もっと見るニュース',

    informationLang: {
      information: 'ニュースと情報',
    },

    marketLang: {
      market: "市場情報",
      name: "名称",
      turnover: "取引量(USDT)",
      price: "最新価格",
      change: "24時間変動",
      trade: "取引に進む",
    },

    functionsLang: {
      functions: "一般的な機能",

      trust: '委託取引',
      transaction: 'API取引',
      service: 'サービス選択',
      promotion: '招待とコミッション',
    },

    partnersLang: {
      partners: 'パートナー'
    },
  },


  ranking: {
    ranking: 'ランキング',
    rankingTabList: [
      { value: 1, label: '週間収益', icon: 'MoneyCollectOutlined' },
      { value: 2, label: '週間ROI', icon: 'StockOutlined' },
      { value: 3, label: '月間収益', icon: 'PayCircleOutlined' },
      { value: 4, label: '月間ROI', icon: 'BarChartOutlined' },
      { value: 5, label: '合計収益', icon: 'AccountBookOutlined' },
      { value: 6, label: '合計ROI', icon: 'FundOutlined' },
      { value: 7, label: '総資産', icon: 'AuditOutlined' },
    ],
    income: "Pnl",
    rate: "ROI"
  },


  strategy: {
    strategy: "量的戦略",
    strategyList: [
      {
        name: 'A01 低リスク低リターン',
        rate: '50%-100%',
        color: "var(--c-main-10)",
        tagColor: "var(--c-main-80)",
        desc: [
          '顧客収益：20%-50% · 年間管理料：2%',
          '無料管理料：VIP3（100万USD）· レバレッジ：0-5',
          '弊社シェア：70%'
        ],
        content: [
          '取引方法：API · 配当期間：四半期 · プロトコル期間：四半期',
          '取引可能な資産：Stablecoins/ETH/BTC'
        ]
      },
      {
        name: 'B01 中リスク中リターン',
        rate: '100%-300%',
        color: "var(--c-main-30)",
        tagColor: "var(--c-main-90)",
        desc: [
          '顧客収益：50%-150% · 年間管理料：2%',
          '無料管理料：VIP3（100万USD）· レバレッジ：0-5',
          '弊社シェア：60%'
        ],
        content: [
          '取引方法：API · 配当期間：四半期 · プロトコル期間：四半期',
          '取引可能な資産：Stablecoins/ETH/BTC'
        ]
      },
      {
        name: 'C01 高リスク高リターン',
        rate: '300%-600%',
        color: "var(--c-main-40)",
        tagColor: "var(--c-main-100)",
        desc: [
          '顧客収益：150%以上 · 年間管理料：2%',
          '無料管理料：VIP3（100万USD）· レバレッジ：5-20',
          '弊社シェア：50%'
        ],
        content: [
          '取引方法：API · 配当期間：四半期 · プロトコル期間：四半期',
          '取引可能な資産：Stablecoins/ETH/BTC'
        ]
      }
    ],
  },

}

export default locale;

