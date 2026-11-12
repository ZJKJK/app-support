# 应用支持与政策

开发者：zhangjiankang  
联系邮箱：zhangjiankang913@gmail.com

站点首页：https://zjkjk.github.io/app-support/

| App | 隐私政策 / Privacy | 用户协议 / Terms | 技术支持 / Support |
| --- | --- | --- | --- |
| 千度阅读 | https://zjkjk.github.io/app-support/qiandu-privacy.html | https://zjkjk.github.io/app-support/qiandu-terms.html | https://zjkjk.github.io/app-support/qiandu-support.html |
| 映页 | https://zjkjk.github.io/app-support/pdfworkbench-privacy.html | https://zjkjk.github.io/app-support/pdfworkbench-terms.html | https://zjkjk.github.io/app-support/pdfworkbench-support.html |
| 岛屿账本 | https://zjkjk.github.io/app-support/islandledger-privacy.html | https://zjkjk.github.io/app-support/islandledger-terms.html | https://zjkjk.github.io/app-support/islandledger-support.html |

## App Store Connect

- “应用隐私 → 隐私政策网址”填写对应隐私政策页面。
- iOS 版本页面的“技术支持网址”填写对应支持页。
- 网站首页可用于可选的“营销网址”，也可以先留空。
- 未配置自定义许可协议时，Apple 标准 EULA 默认适用；本仓库用户协议页面不自动修改 App Store Connect 的许可协议设置。
- App Store 的隐私问卷需要另外按实际 SDK 数据处理填写，发布网站不会自动填写问卷。

## 维护

内容源为 `content.json`，样式为 `style.css`，章节结构由 `legal_documents.py` 统一生成。修改后运行：

```sh
python3 build.py
```

协议页面采用白底正文、居中标题、更新时间、章节及条款编号，重点条款加粗；联系方式保留在正文和文末。排版参考[豆包用户协议](https://www.doubao.com/legal/terms)、[豆包隐私政策](https://www.doubao.com/legal/privacy)及[美团基本功能隐私政策](https://rules-center.meituan.com/m/detail/2)。仅参考文档组织与阅读样式，正文按各 App 实际功能独立维护。

App 内离线阅读资源也由相同内容生成，更新网页正文时同步导出，避免两套内容分离：

```sh
python3 export_native.py --app qiandu --output /path/to/qiandu/Resources/LegalDocuments.json --legacy-output /path/to/qiandu/Resources/Legal.json
python3 export_native.py --app pdfworkbench --output /path/to/PDFWorkbench/Resources/LegalDocuments.json
python3 export_native.py --app islandledger --output /path/to/IslandLedger/Resources/LegalDocuments.json
```

提交生成的 HTML 和内容源。GitHub Pages 使用 `main` 分支的根目录发布，`.nojekyll` 关闭 Jekyll 处理。站点不需要第三方库、广告、浏览器分析脚本或表单服务。网页更新不会自动发布任何 iOS App。

公开仓库仅存放网站内容，不应加入应用配置、密钥或用户文件。
