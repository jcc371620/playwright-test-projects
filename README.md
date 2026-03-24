# playwright-test-projects

本项目用于学习Pytest + Playwright 自动化测试, 目的是能看到模拟硬件测试设备通过61850接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性，并且可以维护测试用例。

---

## Project Structure

<!-- TREE_START -->
<details>
<summary>📂 Project Structure</summary>

```text
├── .gitignore        # Python项目通用忽视规则 (1.0 KB, 2026-03-25)
├── README.md         # playwright-test-projects (11.4 KB, 2026-03-25)
├── allure-results/   (dir, 2026-03-25)
│   ├── 02011478-803a-400c-b3c1-3579b20bd4da-container.json     (0.4 KB, 2026-03-25)
│   ├── 033863f3-6a75-4655-8513-4361d155e696-result.json        (7.6 KB, 2026-03-25)
│   ├── 040a8014-6f05-4841-a028-5c801eccda0e-container.json     (0.4 KB, 2026-03-25)
│   ├── 050d6693-aae1-4c55-8d79-e33431818ee2-container.json     (0.2 KB, 2026-03-25)
│   ├── 08ca90c6-5d86-4bca-8cce-64526dad2caa-container.json     (0.2 KB, 2026-03-25)
│   ├── 0f616289-f52c-4bfa-a4f3-cc6da8079b08-container.json     (0.2 KB, 2026-03-25)
│   ├── 0f88fca2-1614-4ce6-87e3-fa639e120a4a-container.json     (0.4 KB, 2026-03-25)
│   ├── 0fd21bb3-7cf3-4476-aa73-f23d98445b36-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 158e4a73-4eb1-4ec9-8921-944ad91be9b0-container.json     (1.0 KB, 2026-03-25)
│   ├── 1613af79-3109-4694-9dd5-b979826c66b7-result.json        (7.6 KB, 2026-03-25)
│   ├── 16885731-0c72-4b16-8cfe-834ed8c19258-container.json     (0.2 KB, 2026-03-25)
│   ├── 16d55785-58bf-4931-8cb8-e6ac2ec95d9d-container.json     (0.4 KB, 2026-03-25)
│   ├── 16f5c253-aabf-4d23-af61-568784659a97-container.json     (0.2 KB, 2026-03-25)
│   ├── 1894717f-ae09-47be-88a9-d7b78dcfee2d-container.json     (0.4 KB, 2026-03-25)
│   ├── 1b170794-f9c4-4d96-8bee-d196f0bc0a59-container.json     (0.2 KB, 2026-03-25)
│   ├── 1c23978a-909b-4669-b2ec-a18c5c32b52f-container.json     (0.4 KB, 2026-03-25)
│   ├── 1d0fb998-7444-482c-aea6-e7bba60afd34-container.json     (0.2 KB, 2026-03-25)
│   ├── 1e27550c-f689-4689-a339-2893bea6a109-container.json     (0.2 KB, 2026-03-25)
│   ├── 1e8a22d6-5710-4d25-ba60-00b76a36335a-container.json     (0.2 KB, 2026-03-25)
│   ├── 2117e3c1-b4d7-4466-b863-b1c60a0440ce-container.json     (0.4 KB, 2026-03-25)
│   ├── 214f3d9b-69d8-494d-9f04-970b481f5b36-result.json        (7.6 KB, 2026-03-25)
│   ├── 21aebec4-4cd6-4f73-a73e-cfbe5da0f92c-container.json     (0.2 KB, 2026-03-25)
│   ├── 2233fb8f-2767-4d69-89fa-72f90dc0424c-container.json     (0.4 KB, 2026-03-25)
│   ├── 2346139c-1a02-4d60-9914-48cc34d9d1b1-container.json     (0.4 KB, 2026-03-25)
│   ├── 24628ada-f9c5-498b-a9ea-7631be83bf2d-container.json     (0.4 KB, 2026-03-25)
│   ├── 24e15d7f-283c-4693-bf95-0b44cc345d10-container.json     (0.2 KB, 2026-03-25)
│   ├── 268ba20e-8ecc-46ed-9a50-863f40470d80-container.json     (0.4 KB, 2026-03-25)
│   ├── 28457f70-23e3-4cc0-aad4-2b20dcb3826f-container.json     (1.0 KB, 2026-03-25)
│   ├── 2a17ea29-ac5c-4acc-bbd4-1a0c5ceb906c-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 2b22444a-3a9a-46da-8f34-c03cc2124d7a-container.json     (1.0 KB, 2026-03-25)
│   ├── 2b5ae29e-71c3-48e7-a63a-0b19b172a3e8-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 2b66246a-5121-47e5-ab81-bb541d14ed10-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 2f27240f-4641-49f6-9ff0-73cd089a5fa5-container.json     (0.2 KB, 2026-03-25)
│   ├── 2f45ab37-60e6-4892-9112-7a4eb7b03edb-container.json     (0.4 KB, 2026-03-25)
│   ├── 31125cb8-bde5-4c11-929b-d4bcb99fa50d-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 31474c8e-fed2-4437-b75d-c5432c2fe2bc-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 3196ab90-bf51-4455-9070-411ec4818c11-container.json     (0.2 KB, 2026-03-25)
│   ├── 36a37167-16ea-4ae0-8ea6-e4767817ddd4-container.json     (0.4 KB, 2026-03-25)
│   ├── 374a8f25-3ccd-4b66-9969-ca4fc86e4cfa-container.json     (0.2 KB, 2026-03-25)
│   ├── 3829289b-a1cc-4276-8bb5-e09db50cc486-container.json     (0.2 KB, 2026-03-25)
│   ├── 3aaa0ca6-46ca-414c-9593-7f15b39a5944-result.json        (7.6 KB, 2026-03-25)
│   ├── 3aec46ed-4566-45b7-ba04-e618577042d3-container.json     (0.2 KB, 2026-03-25)
│   ├── 3bb6ce33-bcb5-4070-88bc-8bd9a40972f8-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 3c8ae4da-acfb-4dd3-b01f-daec891bad5a-container.json     (0.2 KB, 2026-03-25)
│   ├── 3c94d4d8-73d1-44a2-8208-13fe8fa42b3a-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 3ca8f64b-b92d-4cd7-a3de-a6d88413b475-container.json     (1.1 KB, 2026-03-25)
│   ├── 3f7bd723-5061-4011-8483-39e999f801bd-container.json     (0.2 KB, 2026-03-25)
│   ├── 40f4b831-b63d-4214-b2c0-fc17da22c2b8-container.json     (0.2 KB, 2026-03-25)
│   ├── 43f2bade-5c2d-4277-9dea-32eb39eeceec-container.json     (0.2 KB, 2026-03-25)
│   ├── 49c5fe06-c667-4e90-9a22-723b35d10ae6-container.json     (0.2 KB, 2026-03-25)
│   ├── 4a99a1e8-c979-4b97-8d2f-f76da1f1dbbe-container.json     (0.2 KB, 2026-03-25)
│   ├── 4b5f4138-ebc4-4c57-b58e-d438c7e2a277-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 4c679c80-0c04-4386-bcff-288d769b3e2d-result.json        (7.6 KB, 2026-03-25)
│   ├── 4de34832-7b7e-48d8-b65d-b40a698c9f31-container.json     (0.2 KB, 2026-03-25)
│   ├── 4e0b65ae-1aae-4c7d-ab7e-7b075592df8b-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 4e43dcd4-bc54-4666-9f80-df4bd9a235b9-result.json        (7.6 KB, 2026-03-25)
│   ├── 4e73b7cf-6337-4b49-b0d9-6fbed9592996-container.json     (0.2 KB, 2026-03-25)
│   ├── 4e88eceb-3abc-4532-a407-9c536679d99d-container.json     (0.4 KB, 2026-03-25)
│   ├── 4f94d949-6ca5-4e58-b68d-5d2274c0b589-container.json     (0.2 KB, 2026-03-25)
│   ├── 5284a116-08ba-4f07-a0a4-cf6b77b007fa-container.json     (0.4 KB, 2026-03-25)
│   ├── 52c55584-ddca-4835-9582-bfd4f5ded8bf-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 54413403-1548-4315-99fe-5d2b080908fb-container.json     (0.4 KB, 2026-03-25)
│   ├── 54fa23ba-e345-42c0-a7f1-a53a8923f009-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 555b3272-15b6-4136-bcf5-be2efda5b5fc-container.json     (0.4 KB, 2026-03-25)
│   ├── 55a33f66-536a-4aad-a8ed-34cbf7cfd83a-container.json     (0.2 KB, 2026-03-25)
│   ├── 55c7350c-a0e7-4601-9590-5cac267e89c8-container.json     (0.4 KB, 2026-03-25)
│   ├── 56147975-282d-4396-8e22-d0786fb319f0-container.json     (0.4 KB, 2026-03-25)
│   ├── 58058ddd-7c1f-4254-8423-0eadab18dc25-container.json     (0.2 KB, 2026-03-25)
│   ├── 5b01a72c-683e-4d08-b1f5-675849e38254-result.json        (7.6 KB, 2026-03-25)
│   ├── 5e32a1f3-f370-47a5-a46c-60d0e21254fe-container.json     (0.2 KB, 2026-03-25)
│   ├── 5f762e82-2cdd-4309-a9b9-84b9ceae5bc5-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 5fa30784-429d-436d-950e-9a143bb0a52a-container.json     (0.2 KB, 2026-03-25)
│   ├── 62d2d1b6-c58c-420b-9c2b-947776c0d6ba-container.json     (1.0 KB, 2026-03-25)
│   ├── 63656e34-c77b-4891-aa13-78be95bde04c-container.json     (0.4 KB, 2026-03-25)
│   ├── 6481b605-3ad5-4097-ae06-f430f64e9355-container.json     (0.4 KB, 2026-03-25)
│   ├── 64e8553c-30f9-4476-86a1-4677a38555ad-container.json     (0.4 KB, 2026-03-25)
│   ├── 67deab55-6d6e-460f-a5e9-21701fcec728-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 68debfc4-130c-4d25-a65b-89db7accf938-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 6a21e63c-cf5d-43a5-b82c-49517910d824-container.json     (1.1 KB, 2026-03-25)
│   ├── 6b10744b-d6c2-476c-b0d5-3979c9bcfd9a-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 6fdef691-12b6-4a41-b9ff-9997645d8fc3-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 7107b793-5591-4569-9b6e-89b05807c035-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 71102ac2-6407-489b-80fe-ade4dfd64e91-container.json     (1.0 KB, 2026-03-25)
│   ├── 71bbb621-6058-4abb-adca-f738af5dd6a0-container.json     (0.2 KB, 2026-03-25)
│   ├── 74f583e2-6b41-4382-9aca-771944246c3a-container.json     (0.4 KB, 2026-03-25)
│   ├── 7632963d-cec7-4d0e-9df8-c2deabcd2c00-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 7668c8ee-179e-4353-b7c1-3b10bb80fda3-container.json     (0.2 KB, 2026-03-25)
│   ├── 7824bb4e-eec5-4521-9f29-3989e9978f54-container.json     (0.2 KB, 2026-03-25)
│   ├── 7a3fab0c-e10f-47f4-ad6f-002b8301e2f1-result.json        (7.6 KB, 2026-03-25)
│   ├── 7aee87e6-b8c7-4499-839c-7456019a06b8-result.json        (7.6 KB, 2026-03-25)
│   ├── 7c949554-e7cc-4e60-8698-6ab4625cf337-container.json     (0.4 KB, 2026-03-25)
│   ├── 7cc65d84-8f6f-4786-a35f-65bc8ef62358-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 7eaa6e4b-ce95-43c6-921c-991c0bb28fcb-container.json     (0.4 KB, 2026-03-25)
│   ├── 7fff9864-b9ab-4fd7-8c02-3f8757bbdd55-container.json     (0.2 KB, 2026-03-25)
│   ├── 802fcefc-fbb5-4aad-b988-0ec89a80dcb0-container.json     (0.2 KB, 2026-03-25)
│   ├── 8177fa92-a2f5-4169-b544-ff5f3c539ef8-container.json     (0.2 KB, 2026-03-25)
│   ├── 81ac005a-03b3-45da-9270-758abac3c8f5-container.json     (0.2 KB, 2026-03-25)
│   ├── 83a6d6c4-591f-43ab-8806-070ce0ee0bbf-container.json     (0.2 KB, 2026-03-25)
│   ├── 855c02a0-2c2c-4fe8-9f5c-1b20d3c2cceb-container.json     (0.4 KB, 2026-03-25)
│   ├── 86934b44-82c1-4d9e-a997-0b8d44c32df2-container.json     (0.2 KB, 2026-03-25)
│   ├── 8cd80f35-91da-47df-9c3c-b331587de399-result.json        (7.6 KB, 2026-03-25)
│   ├── 8d1cac23-d370-441f-b9ed-a1fce662efaf-container.json     (0.2 KB, 2026-03-25)
│   ├── 908834e0-ab68-4550-b76a-b0ca139871aa-container.json     (1.0 KB, 2026-03-25)
│   ├── 9206c114-5eab-4e70-bcec-1f3f9cbc2502-container.json     (0.4 KB, 2026-03-25)
│   ├── 92a3df8a-3bb1-4e14-8327-88758c503251-container.json     (0.2 KB, 2026-03-25)
│   ├── 9349b388-509d-441a-87b1-b36cabd3abb5-container.json     (0.2 KB, 2026-03-25)
│   ├── 950d7a81-0c3b-4616-a10f-bd5b6b9630c8-container.json     (1.0 KB, 2026-03-25)
│   ├── 976c084c-6e67-4342-b109-e582434c80b3-container.json     (0.2 KB, 2026-03-25)
│   ├── 9944afe5-3ab6-4f62-adfe-29b44e5abb06-container.json     (0.2 KB, 2026-03-25)
│   ├── 9ab19901-d645-4333-b711-c0106f139966-container.json     (0.4 KB, 2026-03-25)
│   ├── 9b5cebfd-68f5-4aaa-ab59-d05cf1633cca-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 9f0d99de-4053-4581-82c8-f50993cec048-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── a4c110b0-e16d-44cd-b46c-62aaf9879fb5-container.json     (0.2 KB, 2026-03-25)
│   ├── a4e539d6-2f7b-4834-a6ac-8e0219b4dcc5-container.json     (0.2 KB, 2026-03-25)
│   ├── a71fb47e-691f-4137-a1b3-527bc276096a-container.json     (0.2 KB, 2026-03-25)
│   ├── a9ef21cc-bf46-474a-920f-f5ef1b0475e2-container.json     (0.4 KB, 2026-03-25)
│   ├── aa2180de-7c73-40bf-a9e5-cbb90c0637af-container.json     (0.2 KB, 2026-03-25)
│   ├── aed24c68-499b-4921-9fc8-5e019f28103f-result.json        (7.6 KB, 2026-03-25)
│   ├── b043ab7f-b480-4b87-928f-169d8384ea46-container.json     (0.2 KB, 2026-03-25)
│   ├── b16ba229-ec8c-4e3f-92ed-8751a1d51d7f-container.json     (0.4 KB, 2026-03-25)
│   ├── b23e19fa-2c15-413f-a4fe-b0afe4880e51-container.json     (0.2 KB, 2026-03-25)
│   ├── b3f93e29-a7a8-42ba-9fcb-18468d55db35-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── b4f7d268-3395-4123-8f7b-9d69cbaaa9fd-container.json     (0.2 KB, 2026-03-25)
│   ├── b4f94a0b-4f69-420a-9fa4-6be34c7d8c38-container.json     (0.2 KB, 2026-03-25)
│   ├── b57e0272-94e4-43d3-8b22-111f0ca65a90-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── b59d1bfb-60cf-42db-be6a-d3925bdbd7f7-container.json     (0.2 KB, 2026-03-25)
│   ├── b6041774-aa95-489b-98d0-d8efa018479d-container.json     (0.4 KB, 2026-03-25)
│   ├── b6856ed2-c726-4146-8a92-f0991761dbc0-container.json     (0.2 KB, 2026-03-25)
│   ├── b8307a78-0618-48a9-86a8-6b9d61543757-container.json     (0.2 KB, 2026-03-25)
│   ├── b9356eab-6d10-4918-86fe-bdebde0a4e4b-container.json     (0.2 KB, 2026-03-25)
│   ├── b9ca7288-1ddf-4c13-869e-2bd812fff2c2-result.json        (7.6 KB, 2026-03-25)
│   ├── ba30eaf0-de59-4617-aa74-92a87f7ab0d4-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── bbb25c98-4007-408e-a527-623877b3ff9b-container.json     (0.2 KB, 2026-03-25)
│   ├── be57a3e9-ec14-4894-a851-f45f917a29be-container.json     (0.2 KB, 2026-03-25)
│   ├── bf735c81-19ac-4c96-ac35-5025c9fc1c7d-container.json     (0.2 KB, 2026-03-25)
│   ├── c07b8507-0e9e-488f-b295-c82ae48570d6-result.json        (7.6 KB, 2026-03-25)
│   ├── c1752f48-7bec-48f9-b9dd-fe8e93969180-container.json     (0.2 KB, 2026-03-25)
│   ├── c2938311-bc33-4df8-af29-30479a9c26fc-container.json     (0.2 KB, 2026-03-25)
│   ├── c3610cbb-1888-4868-b814-0304a3a6cdd8-container.json     (0.4 KB, 2026-03-25)
│   ├── c3d32066-734d-42c1-8e4c-13f3c7332438-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── c3fac526-06f5-4358-a8fd-103c3dbae161-container.json     (0.2 KB, 2026-03-25)
│   ├── c437cc8a-fb18-411c-b787-d7e20e925514-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── c4979033-509a-4790-ad0b-c9d12fa599fc-container.json     (1.1 KB, 2026-03-25)
│   ├── c523e17e-b89f-4b9f-afde-f1bd123778fb-container.json     (0.4 KB, 2026-03-25)
│   ├── c57d65cf-a5a2-435d-a6d5-e888288ad182-container.json     (0.4 KB, 2026-03-25)
│   ├── cb1b1441-5549-4d5f-9ca2-480158ed90a9-container.json     (0.2 KB, 2026-03-25)
│   ├── cb274b51-c608-49b7-ad61-5846d1dca7af-container.json     (0.4 KB, 2026-03-25)
│   ├── cb2c1011-a984-4f16-9667-f6ce7b95edcd-container.json     (0.2 KB, 2026-03-25)
│   ├── cb707571-6781-4c87-9246-7ae6043a32f2-container.json     (0.4 KB, 2026-03-25)
│   ├── cca5cb5c-d748-4b0d-8fd9-abc534b393ef-result.json        (7.6 KB, 2026-03-25)
│   ├── ccefcd2d-b01d-4028-9cd9-7f3d1d987c76-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── cd8e0ee3-ceee-430a-ae25-fb7829b557b0-container.json     (1.0 KB, 2026-03-25)
│   ├── cdb14183-567c-4176-882e-ebfd27be2a4b-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── cdf6c3e1-6c3a-47b5-ab09-a1024c4a4b23-container.json     (0.2 KB, 2026-03-25)
│   ├── cf5f64d9-8dcf-4970-b1bb-178c0a254f0c-result.json        (7.6 KB, 2026-03-25)
│   ├── cf87764b-a0e8-40b1-be55-91d738d55a11-container.json     (0.2 KB, 2026-03-25)
│   ├── d024683e-d9e5-4a2c-982f-2c6651d3f55a-container.json     (0.2 KB, 2026-03-25)
│   ├── d0dc22e0-7f2c-48c4-b768-600a91fa070b-container.json     (0.2 KB, 2026-03-25)
│   ├── d1014ab8-3fb1-4916-b40c-1c99d617c462-result.json        (7.6 KB, 2026-03-25)
│   ├── d1605e78-dab2-49ce-bc13-c3d3c619750a-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── d2ccc27b-3e6b-4570-b8c6-2117b25c2718-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── d95dff3b-9186-4281-84a2-4581d6a51866-container.json     (0.4 KB, 2026-03-25)
│   ├── d9bb0974-a73a-4725-be8f-da3845ee024c-container.json     (0.2 KB, 2026-03-25)
│   ├── da13d78b-e9bd-4438-b036-589f196b10c7-container.json     (1.0 KB, 2026-03-25)
│   ├── daafc4f6-ac75-45ee-8a8c-ec28730afdd7-container.json     (1.2 KB, 2026-03-25)
│   ├── dc9cd606-29d3-4309-86a6-6f5df5b131cb-container.json     (0.2 KB, 2026-03-25)
│   ├── dca1f981-6357-41eb-9b28-c130fc84adfa-container.json     (0.2 KB, 2026-03-25)
│   ├── ddd6d899-5b2d-433e-8d3a-239d484a99bd-container.json     (1.0 KB, 2026-03-25)
│   ├── e0515bef-d7dc-4875-84c6-b21f7fa4f427-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── e1dc90bc-18d3-47f9-8a55-4e5924033b6d-result.json        (7.6 KB, 2026-03-25)
│   ├── e2c903b8-0f6a-4960-bd58-6053e028ac42-container.json     (0.2 KB, 2026-03-25)
│   ├── e8050dc3-a329-4587-b6c2-7408ddefc89b-container.json     (0.2 KB, 2026-03-25)
│   ├── e85966c7-225a-4239-b44c-84cf8248b959-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── e99ae6bf-9207-420d-abe4-d5af8ac5c962-container.json     (0.2 KB, 2026-03-25)
│   ├── ed19933e-ce4c-4814-8122-33fea3505184-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── ee4e80b9-0c99-49ec-a139-d08efa4956e9-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── eecca837-1d4d-49f9-8d0d-f512f3365a4f-result.json        (7.6 KB, 2026-03-25)
│   ├── eeedc0c7-3a59-4fac-b774-6530ad3ae136-container.json     (0.4 KB, 2026-03-25)
│   ├── efe7d2d3-a490-4271-a5b7-1cebcc6d6153-container.json     (0.4 KB, 2026-03-25)
│   ├── f23f7b0b-41d3-4f6c-8335-e3f7af1f80d8-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── f2505489-9aca-4661-887e-33eb0189be8f-container.json     (0.2 KB, 2026-03-25)
│   ├── f2f4cfb2-1df4-4574-bf18-3457fd224136-container.json     (0.4 KB, 2026-03-25)
│   ├── f3104e72-9c0e-41fb-8388-9a07b7712799-container.json     (0.2 KB, 2026-03-25)
│   ├── f35700cd-e867-4095-82d9-c80a48b201d3-result.json        (7.6 KB, 2026-03-25)
│   ├── f38744c9-df9a-49ae-b247-8732fc9ecc4b-result.json        (7.6 KB, 2026-03-25)
│   ├── f3b6a514-1bc8-4be0-8dd9-95f2c74b8ba0-container.json     (0.2 KB, 2026-03-25)
│   ├── f3c51611-8df0-49f0-af8b-1cc3e02228e6-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── f4d750b1-4d97-4d54-b147-b6405cba36a8-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── f5653075-0588-435d-be5a-8c53f1dd52ac-container.json     (0.2 KB, 2026-03-25)
│   ├── f6cee86b-1820-4f93-b60c-68a47b15edeb-container.json     (0.2 KB, 2026-03-25)
│   ├── fa909b5e-107f-4303-ae9d-2b52c3e8d2ca-container.json     (0.2 KB, 2026-03-25)
│   ├── fad2df9c-85a1-40f0-a80e-33ac83a2b492-container.json     (0.2 KB, 2026-03-25)
│   ├── fb5839ef-b571-4901-868f-37f0e36aeeb3-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── fb7f58a9-b101-46f7-85bd-1863d0f2bb7a-container.json     (0.2 KB, 2026-03-25)
│   └── ff117ecd-0d93-4744-926e-ff7fbf3d5f8e-attachment.attach  (0.0 KB, 2026-03-25)
├── conftest.py       # Pytest 全局配置文件及 Fixtures (2.0 KB, 2026-03-25)
├── data/             (dir, 2026-03-25)
│   └── test_cases.py  # data/test_cases.py (8.1 KB, 2026-03-25)
├── generate_tree.py  # 每次 git commit 自动更新 README (6.0 KB, 2026-03-25)
├── lib/              (dir, 2026-03-25)
│   ├── ai_analyzer.py      # AI 分析器模块 (2.9 KB, 2026-03-25)
│   └── iec61850_client.py  # IEC 61850 客户端模块 (4.8 KB, 2026-03-25)
├── reports/          (dir, 2026-03-25)
│   ├── Execution_Summary_20260325_011944.html      (120.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012715.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012717.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_013012.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_015339.xlsx  (6.6 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020159.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020611.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_022508.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_022809.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_023112.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_023344.xlsx  (7.4 KB, 2026-03-25)
│   ├── Quality_Report_20260325_011944.xlsx         (5.9 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012715.html     (31.0 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012717.html     (120.1 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_013012.html     (119.7 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_015339.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020159.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020611.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_022508.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_022809.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_023112.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_023344.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014556.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014614.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014824.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014842.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_015209.html          (118.8 KB, 2026-03-25)
│   ├── report_20260325_004710.html                 (120.1 KB, 2026-03-25)
│   ├── summary_20260325_004710.xlsx                (5.7 KB, 2026-03-25)
│   └── 硬件监控测试报告_20260325_003851.html               (123.1 KB, 2026-03-25)
├── run.py            # 项目运行入口 (4.9 KB, 2026-03-25)
└── tests/            (dir, 2026-03-25)
    └── test_hardware_to_web.py  # 测试脚本 (3.7 KB, 2026-03-25)
```

</details>
<!-- TREE_END -->
















---

## 学习步骤
### 1. promt
* 准备一个自动化测试项目，目的是希望看到硬件测试设备通过接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性。
一共实现20个test case，case你来决定，test case可以放在单独的文件里方便维护。
全部用python语言。
必须调用61850接口，必须需要使用到playwright，必须能肉眼看到页面交互。
告诉我详细的建立文件的步骤，项目结构，代码里的注释尽可能详细，最好每一个行为都要有注释，比如用了fixture就注释说一下为什么用。从零开始细节教学，如果有专业术语必须要解释并且双语。文件夹根目录为playwright-test-projects

### 2. 激活虚拟环境
* python3 -m venv venv //这条命令会在文件夹里生成一个名为 venv 的文件夹，存放这个项目专用的 Python。
* source venv/bin/activate // 行完这个，你会发现终端提示符前面多了个 (venv) 字样，说明你已经进入了“样板间”。

### 3. 安装依赖
* python generate_tree.py --install
* 由于 iec61850-client 在 Windows/Python 环境下安装极易出错（涉及 C 编译），我们在教学中采用 Scapy 库来模拟 61850 报文，这是安全和测试领域最专业的工具。

```
# 安装 Scapy 用于处理 61850 报文
pip install scapy 

# 安装 Playwright 自动化框架
pip install playwright

#pyminimms 是一个常用的 Python 61850/MMS 库；openai 用于 AI 分析。
playwright install chromium

# 安装 OpenAI SDK 用于 AI 分析
pip install openai

# 安装 Flask 用于模拟 Web 后台接口
pip install flask

pip install scapy playwright pytest pytest-playwright python-dotenv openai

#生成报告
pip3 install pytest-html
pip install pandas openpyxl
pip install allure-pytest

#安装allure
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install allure
allure --version

#查看报告
allure serve allure-results

```

---

## 学习笔记梳理

### 1. playwright专业术语
* Browser Instance
* Browser Context
* Browser Page
* Playwright Locator
* Auto-waiting // 在你执行 click() 或 fill() 之前，Playwright 会自动检查元素是否：Visible (可见)、Attached (已挂载到 DOM)、Stable (动画已停止)、Enabled (非禁用状态)。如果不满足，它会持续重试直到超时。
* Test Fixtures // 它包含 Setup (执行前准备) 和 Teardown (执行后清理)。例如 page 就是一个内置 Fixture，它帮你自动处理了浏览器启动和关闭。
* Web-First Assertions // 它们是异步且会自动重试的。例如 await expect(locator).toBeVisible() 不会立即失败，它会反复检查元素是否出现，直到达到设定的超时时间（默认 5 秒）。
* Codegen // 打开一个浏览器，你在网页上的所有点击、输入都会在侧边窗口同步生成高质量的 Playwright 代码。
* Trace Viewer // 它记录了测试运行的每一个瞬间。你可以查看到每一步操作前后的 DOM 快照、Network (网络请求)、Console (控制台日志)。
* Storage State // 你可以先登录一次，将 Cookie 和 LocalStorage 保存为一个 JSON 文件。之后的几百个测试用例直接加载这个 JSON，跳过登录步骤。
* Parallelization //Playwright 默认根据 CPU 核心数启动多个 Worker Processes (工作进程) 同时运行测试。

### 2. IEC 61850标准
* 👉 IEC 61850 = 标准（Standard）它里面包含了协议、数据模型、通信规则等一整套规范。
* IED (Intelligent Electronic Device): 智能电子设备（如施耐德的保护继电器）。
* MMS (Manufacturing Message Specification): 制造报文规范（61850 传输数据的核心协议）。
* Dataset (数据集): IED 中打包传输的一组逻辑值（如电压、电流）。
* Logical Node (LN): 逻辑节点（设备功能的最小单位，如测量节点 MMXU）。
* Data Consistency Check: 数据一致性检查（验证协议层和 UI 层数据是否同步）。

---

### 2. 工业专业术语
* 由于 iec61850-client 在 Windows/Python 环境下安装极易出错（涉及 C 编译），我们在教学中采用 Scapy 库来模拟 61850 报文，这是安全和测试领域最专业的工具。

---

## 问题与解决方法
### 1. 在sync的时候有弹窗报错：
* 归因：vpn不稳定导致
* 解决步骤：
    1. 报错弹窗
    2. Show Command Output查看报错信息
    3. > git pull --tags origin main
fatal: unable to access 'https://github.com/jcc371620/playwright-test-projects.git/': Failed to connect to github.com port 443 after 21054 ms: Could not connect to server
    4. gemini分析

### 2. .git/hooks/pre-commit
* 归因： .git/hooks/ 是本地目录，不会被 Git 提交，不会跟着仓库同步
* 解决步骤：
    1. 第一步：进入 hooks 目录 // cd .git/hooks
    2. 创建 pre-commit：
        Linux / Mac / Git Bash: touch pre-commit
        Windows: New-Item pre-commit
    3. 写内容： 
        #!/bin/sh
        python generate_tree.py
        git add README.md
    4. 给执行权限：
        chmod +x pre-commit
    5. 验证是否生效：
        git commit -m "test"