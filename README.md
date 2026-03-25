# playwright-test-projects

本项目用于学习Pytest + Playwright 自动化测试, 目的是能看到模拟硬件测试设备通过61850接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性，并且可以维护测试用例。

---

## Project Structure

<!-- TREE_START -->
<details>
<summary>📂 Project Structure</summary>

```text
├── .gitignore        # Python项目通用忽视规则 (1.0 KB, 2026-03-25)
├── README.md         # playwright-test-projects (15.0 KB, 2026-03-25)
├── allure-results/   (dir, 2026-03-25)
│   ├── 017aaac7-99c1-4dce-a524-80257259f4b5-container.json     (0.2 KB, 2026-03-25)
│   ├── 0454dede-2cd6-42ef-9c41-d8c94b1caecc-container.json     (0.2 KB, 2026-03-25)
│   ├── 04b9ccf4-336e-4167-b7ea-a6f187775720-container.json     (1.0 KB, 2026-03-25)
│   ├── 0598d681-979b-431d-b28b-8b4893e42ff1-container.json     (0.4 KB, 2026-03-25)
│   ├── 0719ee00-61c7-4b7f-864e-45854336ad42-container.json     (1.0 KB, 2026-03-25)
│   ├── 07b9ffa6-9e1b-40f8-990f-018a19f9327b-container.json     (0.4 KB, 2026-03-25)
│   ├── 08cd49fe-5144-4bcd-9d89-927ca72a6cf7-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 09d8745d-97d6-43e3-bfbb-b96de5ef3c00-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 0a537548-403b-4cd7-9096-b58a86a31220-container.json     (0.4 KB, 2026-03-25)
│   ├── 0aad8fc3-b5ce-47df-88db-297ea416ee7b-container.json     (1.0 KB, 2026-03-25)
│   ├── 0b3a80cd-6e25-4b3e-8632-b3b4bde9fec8-result.json        (7.6 KB, 2026-03-25)
│   ├── 0bacd522-af92-48b1-b470-19f67f99780e-container.json     (0.2 KB, 2026-03-25)
│   ├── 0cad8fc7-6a65-41e4-beb9-214d44010851-container.json     (0.2 KB, 2026-03-25)
│   ├── 0d0a4f28-5298-475f-a649-081b67489df6-container.json     (0.2 KB, 2026-03-25)
│   ├── 1034e7f3-d6a0-4b6a-98d7-0e6d97989f02-result.json        (7.6 KB, 2026-03-25)
│   ├── 118239b8-75fd-4c4b-961b-b2a7be76deff-container.json     (0.2 KB, 2026-03-25)
│   ├── 11c5c316-24e9-4665-8ec9-8a80dc29a5dc-result.json        (7.6 KB, 2026-03-25)
│   ├── 14d7c7d8-2515-4001-b6c4-dbe6de7a40ed-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 1717c5cc-19c5-42ee-bf74-797391731823-result.json        (7.6 KB, 2026-03-25)
│   ├── 18182c68-baaf-445f-9aa6-b244bbf7ffe7-container.json     (0.2 KB, 2026-03-25)
│   ├── 18571964-a7aa-4117-90ab-ab0d42ed8a0a-container.json     (0.2 KB, 2026-03-25)
│   ├── 185dcc9c-7cc7-4eff-824a-ebf1fd4d8fd6-container.json     (0.4 KB, 2026-03-25)
│   ├── 18a6bec6-cd68-4886-9f70-204943c33465-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 1cc39d8c-9ce7-4f05-bee2-a04671e3e8cd-container.json     (1.0 KB, 2026-03-25)
│   ├── 1d923060-2079-457e-af64-7aa575646b0c-container.json     (0.4 KB, 2026-03-25)
│   ├── 1e5252d6-1838-48fd-aab8-49bdf26d1d0c-container.json     (0.4 KB, 2026-03-25)
│   ├── 1f0ebee6-c498-4db0-b1fd-470ca765c1ce-container.json     (1.0 KB, 2026-03-25)
│   ├── 222ceb77-27b9-4df0-80f7-d183c0379779-container.json     (0.4 KB, 2026-03-25)
│   ├── 2272ba5d-f1aa-493b-87c0-52696fa38afb-container.json     (0.4 KB, 2026-03-25)
│   ├── 238a680e-2a7e-4af3-86a1-71feed6cf2f1-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 250da409-843f-4c13-95f3-82f93c06b918-container.json     (0.2 KB, 2026-03-25)
│   ├── 25d82da1-792f-47d3-8942-5e1285075748-container.json     (0.4 KB, 2026-03-25)
│   ├── 274465c2-e8e7-4a60-8040-c85ef1d58d7e-container.json     (0.2 KB, 2026-03-25)
│   ├── 29dcf0c6-c90f-48ee-a64d-5e1ac5029350-container.json     (0.2 KB, 2026-03-25)
│   ├── 29e22bf0-6a20-4af6-a6d4-04fc2dd1c520-container.json     (0.2 KB, 2026-03-25)
│   ├── 2af151a4-a1bf-40fb-891e-299ea7875c05-container.json     (0.4 KB, 2026-03-25)
│   ├── 2c2e6d9c-a870-42f8-84b3-defd9579125b-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 2e920a3c-95f6-4ccf-ad95-e3fb67c39c47-container.json     (0.2 KB, 2026-03-25)
│   ├── 2ea4eb92-7802-4a53-af2c-8a47d3af482f-container.json     (0.2 KB, 2026-03-25)
│   ├── 304e4be0-46f4-41c0-94f4-5842b4f8b70a-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 31156dc8-b224-4f89-b044-ab088358c386-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 31b88cff-dcde-45b8-ae8f-554d129bec87-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 32efe2ce-14ab-46a0-b249-be37f3574b94-container.json     (0.2 KB, 2026-03-25)
│   ├── 33ed58ef-b885-4eed-8621-b3bbd9f6fab7-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 354ea19a-c57b-4622-a319-dd1511bd1d00-container.json     (0.2 KB, 2026-03-25)
│   ├── 355e5364-db3d-43da-9506-7f002a572724-container.json     (0.2 KB, 2026-03-25)
│   ├── 35a0d0bd-41b6-41f9-8230-2ccf8a1d5fcb-container.json     (0.2 KB, 2026-03-25)
│   ├── 367940bd-866d-44aa-b5e5-c9b5b08d10d9-container.json     (0.2 KB, 2026-03-25)
│   ├── 376971ad-3ca1-40d0-831c-558787a13c49-container.json     (0.2 KB, 2026-03-25)
│   ├── 3bcc08f6-ddaf-4cc2-babd-f89a7fa527a8-container.json     (0.2 KB, 2026-03-25)
│   ├── 3cb05d0a-4cb1-4167-bbe1-8205dc141e05-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 3da56b29-85df-41eb-a45b-d83e00ee94b1-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 3f96d6a7-7db7-4179-8b19-e48686048e7c-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 3f97accc-e4b7-4c99-b501-a96aa083ea21-container.json     (0.2 KB, 2026-03-25)
│   ├── 411aef92-f106-4af3-91b8-2e92749d1d72-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 417ad3ae-2e21-4b6e-ba0c-3877f01420d4-result.json        (7.6 KB, 2026-03-25)
│   ├── 42c02f49-4915-4dc7-9047-cb553677a296-container.json     (1.1 KB, 2026-03-25)
│   ├── 438878c3-af5e-4d83-83e8-91975ab5f3c9-container.json     (0.4 KB, 2026-03-25)
│   ├── 446a53d3-81bf-41bf-a126-0d8126cca834-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 4526bd57-083f-4f29-b7b1-9e91d323958e-container.json     (0.2 KB, 2026-03-25)
│   ├── 464b486f-da1c-45ae-b73d-ddc4ac0e7f7d-container.json     (0.4 KB, 2026-03-25)
│   ├── 469f1927-7cba-4312-860d-c5230efbb049-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 48d9eb11-f7d4-48a7-b0c0-067026143148-container.json     (0.4 KB, 2026-03-25)
│   ├── 4a19f745-a2a2-44ed-b5a0-0fde492cd804-container.json     (0.2 KB, 2026-03-25)
│   ├── 4ade129b-e8cc-4445-a668-02d20131d847-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 4ca96fb4-a7b1-4c08-8e5c-7b9be04e7fe5-container.json     (0.4 KB, 2026-03-25)
│   ├── 4cea35fe-ac8b-486b-8445-73aef9352bc2-container.json     (0.2 KB, 2026-03-25)
│   ├── 4dc394ca-ee65-4d62-aa10-1595744cabf8-result.json        (7.6 KB, 2026-03-25)
│   ├── 4f692d67-d9f4-4a7d-a654-161f688efcaf-container.json     (0.2 KB, 2026-03-25)
│   ├── 4fccec99-5629-4d80-a543-de95be15a63c-container.json     (0.4 KB, 2026-03-25)
│   ├── 50b180a9-4e6a-4c4f-a4bd-3d1f9e13bba9-container.json     (0.4 KB, 2026-03-25)
│   ├── 53492c19-2bbf-4421-94e1-5fa28156e79b-container.json     (0.2 KB, 2026-03-25)
│   ├── 535066fd-2589-4c47-96c2-815dab4fc34d-container.json     (0.4 KB, 2026-03-25)
│   ├── 538b4d7e-0a31-4b76-af04-64137f7c2497-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 54206c37-8ad8-4a84-9df2-a47781c4f42b-container.json     (0.2 KB, 2026-03-25)
│   ├── 5687ddb7-d950-4d0e-9d81-40ffaaef2eb0-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 57018fc8-338d-4e7a-91b7-d4db31690a1f-container.json     (0.2 KB, 2026-03-25)
│   ├── 579e0965-7856-4cfe-9dd3-f1f0c42782df-container.json     (0.2 KB, 2026-03-25)
│   ├── 5822cfd7-473c-429b-8421-8bd7578ef75b-container.json     (0.2 KB, 2026-03-25)
│   ├── 5988d1b5-cad2-4c86-acf5-259a82407783-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 59c47724-9b6e-43b2-af22-6d082553dc93-container.json     (0.4 KB, 2026-03-25)
│   ├── 5a15bbfa-3b6c-4783-848b-a4e58c6f34da-container.json     (0.4 KB, 2026-03-25)
│   ├── 5a4a1572-2d24-4447-99af-bf1c2f98489b-container.json     (0.2 KB, 2026-03-25)
│   ├── 5a88edcb-efbc-40d0-b3e8-5d73092d0e49-container.json     (0.2 KB, 2026-03-25)
│   ├── 5be4d5c5-7e03-4b56-b8ab-a70d200128f9-container.json     (0.2 KB, 2026-03-25)
│   ├── 5e314dc7-864b-45a4-978c-060e54ad0ad9-container.json     (0.2 KB, 2026-03-25)
│   ├── 608649a9-5eb7-4171-9b06-e77cb1742d5e-container.json     (0.2 KB, 2026-03-25)
│   ├── 61d734c2-3d6c-4693-b794-dc12e00d7599-container.json     (0.4 KB, 2026-03-25)
│   ├── 637849ae-0821-4df2-ab62-240eab4801c1-container.json     (0.2 KB, 2026-03-25)
│   ├── 67a59066-57e1-42da-8bf1-c0dfbfee2601-result.json        (7.6 KB, 2026-03-25)
│   ├── 6bd55924-8576-4583-aaa9-20e39f01db40-container.json     (0.4 KB, 2026-03-25)
│   ├── 6d66eb86-84ec-4630-bea4-121a1cd6ac87-result.json        (7.6 KB, 2026-03-25)
│   ├── 6f92a8c5-73c9-4245-92c2-80170c8e0c7c-result.json        (7.6 KB, 2026-03-25)
│   ├── 7154bd05-5a24-4996-9323-76476c1806a8-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 731e6e55-3d61-46ac-829e-2808c8d44db1-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 7375bc61-701e-4696-98eb-76033b83be2b-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 737e5abd-9eba-4cc8-9037-2aae51df7345-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 75ea3f50-7bef-484c-bd11-63c99148ac53-container.json     (0.4 KB, 2026-03-25)
│   ├── 76241a78-fd58-49eb-ba51-81415d3311b9-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 775bdebd-37b1-410f-acfa-727367e3fb70-container.json     (1.2 KB, 2026-03-25)
│   ├── 789ea658-9845-498b-a7d3-bd5fe4f87cf0-container.json     (0.4 KB, 2026-03-25)
│   ├── 7abbe05d-3893-472f-a03a-71ec4d3b9fc9-container.json     (0.2 KB, 2026-03-25)
│   ├── 7c479301-0dea-41e4-9236-2e6c8a0f661a-container.json     (0.2 KB, 2026-03-25)
│   ├── 7ca6384a-3c3d-4c37-885f-846bfbd13dc5-container.json     (0.2 KB, 2026-03-25)
│   ├── 7d085f82-7365-4ccc-8ff6-3e45b4ae900f-result.json        (7.6 KB, 2026-03-25)
│   ├── 7d94127d-cd90-465d-b1c3-d54171a21d6a-container.json     (0.2 KB, 2026-03-25)
│   ├── 7df95e97-f8ac-4cf7-b0d9-85dfa5885619-result.json        (7.6 KB, 2026-03-25)
│   ├── 7e6c763b-2f21-4c96-afb4-d544def26ebe-container.json     (0.2 KB, 2026-03-25)
│   ├── 7f4f013f-373f-48aa-80b1-b88fff11c2e4-container.json     (0.2 KB, 2026-03-25)
│   ├── 80d89da5-74f4-4f3f-9436-c9af51ba902d-result.json        (7.6 KB, 2026-03-25)
│   ├── 82e9e65f-345f-4ee9-9784-263f5f796d19-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 834cde5f-9d84-4095-ad85-8bdab9af68bd-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 83da8194-be92-4fd7-8b39-ae21caab2350-container.json     (1.0 KB, 2026-03-25)
│   ├── 83ea11fa-4fe4-4dc1-b8b1-d659de81a7ec-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 84227277-9453-40fd-9015-12d728f93c40-container.json     (0.4 KB, 2026-03-25)
│   ├── 86371d4a-2d81-48fc-b05e-76c769cc39f8-container.json     (0.2 KB, 2026-03-25)
│   ├── 8a291ea7-2bdc-4c86-a4ad-6285929974b7-container.json     (0.2 KB, 2026-03-25)
│   ├── 8cd1a38d-1395-430c-9994-3c3a73d885bf-container.json     (0.2 KB, 2026-03-25)
│   ├── 8d2954be-2ec8-4986-9a6e-7e34c9444730-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 8dd099dd-01b5-4ead-bb2e-f50725ee7e9c-result.json        (7.6 KB, 2026-03-25)
│   ├── 906ea604-b0a2-4dac-baf4-bf179a80b631-container.json     (0.2 KB, 2026-03-25)
│   ├── 93a644ff-6c06-4957-9b9e-c28073e21b9c-container.json     (0.4 KB, 2026-03-25)
│   ├── 947bcdf6-36c7-4064-bdee-0aa651f9ea40-container.json     (0.2 KB, 2026-03-25)
│   ├── 95749727-92b8-4ddb-8804-2ec1c255832f-container.json     (0.4 KB, 2026-03-25)
│   ├── 960fee9f-8666-4790-81ed-7b096c8b6a46-container.json     (0.4 KB, 2026-03-25)
│   ├── 99d090ed-5d97-46ab-b05a-dd449633bf92-result.json        (7.6 KB, 2026-03-25)
│   ├── 9ab37fac-c5ee-4e4a-98ff-b42905e558c9-container.json     (0.2 KB, 2026-03-25)
│   ├── 9cf31bcd-2dd3-45c2-b73c-eb761a456f64-result.json        (7.6 KB, 2026-03-25)
│   ├── 9d4c862e-5150-4881-af5f-e28c9f76c200-container.json     (0.2 KB, 2026-03-25)
│   ├── 9f4f2400-9aea-4d0a-8ea4-004a7aaf3347-container.json     (0.2 KB, 2026-03-25)
│   ├── 9fade8f4-279e-464b-a472-4621ca025f67-container.json     (0.2 KB, 2026-03-25)
│   ├── a1060375-e4b4-41f1-9f77-d42cd8720806-container.json     (0.4 KB, 2026-03-25)
│   ├── a28ad5c7-24bf-4aaf-a94f-6df82f981503-container.json     (0.4 KB, 2026-03-25)
│   ├── a368fb60-bd8f-424c-ab10-68403046ec26-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── a81e541b-1d75-4de5-9037-3f34de40656a-container.json     (1.0 KB, 2026-03-25)
│   ├── a98e3cc4-c018-4339-8f46-cf4ad440da2e-container.json     (1.1 KB, 2026-03-25)
│   ├── ad217d30-9b35-44ff-80c8-23abbfe65b36-container.json     (0.2 KB, 2026-03-25)
│   ├── b06b811d-7a01-4575-b714-2d5f00c4d143-result.json        (7.6 KB, 2026-03-25)
│   ├── b1030f2e-b91c-432c-9cf7-fdc2336aa1e9-container.json     (0.2 KB, 2026-03-25)
│   ├── b1920d0c-8880-4cba-be3e-4204c3a7778b-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── b1e8df43-6218-43d4-a0c6-42453e459835-container.json     (0.4 KB, 2026-03-25)
│   ├── b3726a4b-e86a-4893-aa45-8e06243537a6-container.json     (0.4 KB, 2026-03-25)
│   ├── b3e1c942-2942-4194-bac9-206a44116d29-container.json     (0.4 KB, 2026-03-25)
│   ├── b4c68f29-9f7a-48c7-97c5-7a52489f05f4-container.json     (0.2 KB, 2026-03-25)
│   ├── b7d579fd-3b29-4760-ad0e-c7809872eca5-container.json     (0.2 KB, 2026-03-25)
│   ├── b80aba45-a34c-4490-a4aa-304dea39e602-result.json        (7.6 KB, 2026-03-25)
│   ├── ba8acd44-ed64-4092-94af-3ac014dde3d6-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── be5d1a9f-1edd-425a-a544-fd9c4b681fbf-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── c11f3bae-79df-41a8-aaf3-f76935f4444e-container.json     (0.2 KB, 2026-03-25)
│   ├── c81963e8-ef8d-469c-8d96-7a6598e10f66-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── c9104012-b21c-43a2-b217-01eaac487e43-container.json     (0.2 KB, 2026-03-25)
│   ├── c938ffe1-cc78-4455-b3d4-5bc0b7cdc63a-container.json     (0.2 KB, 2026-03-25)
│   ├── ca1f2023-a5b5-4623-bd89-45150c694045-container.json     (0.2 KB, 2026-03-25)
│   ├── caf88ab8-41a5-4578-a951-6f32511de5d8-container.json     (0.2 KB, 2026-03-25)
│   ├── cb31b0bd-0cde-4724-84bf-b33c8a1ec528-container.json     (1.0 KB, 2026-03-25)
│   ├── cd003bc1-0fce-4a0e-8ba7-5b3fb1683ae5-container.json     (0.4 KB, 2026-03-25)
│   ├── cd0618d0-6e4a-4691-b81b-d23493850b47-container.json     (0.2 KB, 2026-03-25)
│   ├── cf10404b-c854-44ce-bf93-48d2a41893b5-container.json     (0.2 KB, 2026-03-25)
│   ├── d0c1f29e-b093-42ff-a214-2c61f8d02955-result.json        (7.6 KB, 2026-03-25)
│   ├── d5320849-dba0-4300-9849-f8d298eb7a2d-container.json     (0.2 KB, 2026-03-25)
│   ├── d55b10e6-6524-4d1c-bb3b-e35b42b2e364-container.json     (0.2 KB, 2026-03-25)
│   ├── d608946c-6e61-4e37-b3f3-fd79c5415c72-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── d7b292c9-5fbb-46ed-ad98-7fc8ea0b929f-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── d8c41a9a-25c2-4373-9e96-490889143bd8-container.json     (0.4 KB, 2026-03-25)
│   ├── da7d1703-3121-490b-9821-2bdadf355b21-container.json     (1.1 KB, 2026-03-25)
│   ├── daef9b3f-9145-4930-8efa-c2490f1b62fe-container.json     (0.2 KB, 2026-03-25)
│   ├── db257929-260d-4565-87d3-bdf327aaaf3a-container.json     (0.2 KB, 2026-03-25)
│   ├── ddce10f0-e297-4e7d-9c14-137f675e17b8-result.json        (7.6 KB, 2026-03-25)
│   ├── e09397ca-8ba6-48a8-a501-d645b86271de-container.json     (0.4 KB, 2026-03-25)
│   ├── e2c5b8e2-f420-4646-9efa-cae53dbc36f9-container.json     (0.2 KB, 2026-03-25)
│   ├── e3928d1d-0c3d-4faf-8eac-ba2b943ab143-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── e710f472-e9d7-4aea-925b-a11f7d92de92-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── e7c9e339-6878-4065-978d-5a7f8cebd622-container.json     (0.2 KB, 2026-03-25)
│   ├── e8853888-798a-4728-b897-21bdcf5c12f8-container.json     (0.2 KB, 2026-03-25)
│   ├── e8e52163-f441-461b-8cb4-ab4625a9ffee-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── e9ee8ab0-eadb-4ff7-b39c-301bdc0b9717-container.json     (0.4 KB, 2026-03-25)
│   ├── ea1ddf9c-b767-434d-8dc1-1e5b59a79c8f-result.json        (7.6 KB, 2026-03-25)
│   ├── f01c5110-6cd0-4ef6-81b2-bc9766506481-container.json     (0.2 KB, 2026-03-25)
│   ├── f1221161-b92b-4702-bae2-3202fda9d869-container.json     (0.2 KB, 2026-03-25)
│   ├── f214f7e8-ac07-4693-8735-9a3631f5bf92-container.json     (1.0 KB, 2026-03-25)
│   ├── f25a14a2-d63e-4e46-ac14-c349aa22553f-container.json     (0.4 KB, 2026-03-25)
│   ├── f35053d2-8a27-46e8-a76a-f2b637e5a170-container.json     (0.2 KB, 2026-03-25)
│   ├── f57eb0be-46b4-4ad5-8b4a-fc5e41611d73-container.json     (0.4 KB, 2026-03-25)
│   ├── f5ccd0c6-eda2-41ad-b22c-ecb01541aba7-container.json     (0.2 KB, 2026-03-25)
│   ├── f5fc50a8-a329-4109-a97d-183f098549f0-container.json     (0.4 KB, 2026-03-25)
│   ├── f6bbaea9-2991-42e6-881c-88ad79c6efa3-container.json     (0.2 KB, 2026-03-25)
│   ├── f8a0bc3c-3b65-478a-b11b-ef559f3e451d-container.json     (0.2 KB, 2026-03-25)
│   ├── f8d5b809-11f6-4e4d-8819-423f5a8a4622-container.json     (0.2 KB, 2026-03-25)
│   ├── f8dadcd9-f188-4e3e-b26d-5e2f31637147-container.json     (0.2 KB, 2026-03-25)
│   ├── f9560678-f825-4f79-b0bf-a9d0a9e92dc1-container.json     (1.0 KB, 2026-03-25)
│   ├── f994af79-5543-4fa6-9d11-bce45a275a55-container.json     (0.2 KB, 2026-03-25)
│   ├── faa7c738-6dcd-4e1b-b36f-401422bc1a75-container.json     (0.4 KB, 2026-03-25)
│   ├── fd725d7a-d4e9-4864-bd85-aa4378bb3e67-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── feb27646-7678-4e5d-b619-7c1defcc9606-container.json     (0.2 KB, 2026-03-25)
│   └── fef1f4a4-9207-4bd9-a646-6f12b6f10248-container.json     (0.2 KB, 2026-03-25)
├── conftest.py       # Pytest 全局配置文件及 Fixtures (2.0 KB, 2026-03-25)
├── data/             (dir, 2026-03-25)
│   └── test_cases.py  # data/test_cases.py (8.1 KB, 2026-03-25)
├── generate_tree.py  # 每次 git commit 自动更新 README (6.0 KB, 2026-03-25)
├── lib/              (dir, 2026-03-25)
│   ├── ai_analyzer.py      # AI 分析器模块 (2.9 KB, 2026-03-25)
│   └── iec61850_client.py  # IEC 61850 客户端模块 (4.8 KB, 2026-03-25)
├── mock_site/        (dir, 2026-03-25)
│   └── index.html  (0.6 KB, 2026-03-25)
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
│   ├── QA_Integration_Report_20260325_024102.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_025135.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_025829.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_151628.xlsx  (7.4 KB, 2026-03-25)
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
│   ├── Technical_Evidence_20260325_024102.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_025135.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_025829.html     (127.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_151628.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014556.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014614.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014824.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014842.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_015209.html          (118.8 KB, 2026-03-25)
│   ├── report_20260325_004710.html                 (120.1 KB, 2026-03-25)
│   ├── summary_20260325_004710.xlsx                (5.7 KB, 2026-03-25)
│   └── 硬件监控测试报告_20260325_003851.html               (123.1 KB, 2026-03-25)
├── run.py            # run.py (4.9 KB, 2026-03-25)
└── tests/            (dir, 2026-03-25)
    └── test_hardware_to_web.py  # test_hardware_to_web.py (3.8 KB, 2026-03-25)
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