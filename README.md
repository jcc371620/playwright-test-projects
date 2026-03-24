# playwright-test-projects

本项目用于学习Pytest + Playwright 自动化测试, 目的是能看到模拟硬件测试设备通过61850接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性，并且可以维护测试用例。

---

## Project Structure

<!-- TREE_START -->
<details>
<summary>📂 Project Structure</summary>

```text
├── .gitignore        # Python项目通用忽视规则 (1.0 KB, 2026-03-25)
├── README.md         # playwright-test-projects (26.7 KB, 2026-03-25)
├── allure-results/   (dir, 2026-03-25)
│   ├── 02ec59f9-81d4-41b6-90e5-ee1d9c823e8d-container.json     (0.2 KB, 2026-03-25)
│   ├── 03af0c97-cd82-4062-a485-0032ce09d7c6-container.json     (0.4 KB, 2026-03-25)
│   ├── 04cf8d8c-6214-49e5-a34e-b55b7e57aca4-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 066bfc62-e698-465b-b236-1e79f85121c4-container.json     (0.2 KB, 2026-03-25)
│   ├── 0761b943-43bf-4b15-b061-7c1f3243312d-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 087e3273-a6a2-41e6-80c9-f09ba2a9c3f3-container.json     (0.4 KB, 2026-03-25)
│   ├── 0dec4dce-0cbd-492e-9eea-fd76507fc72f-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 0f72c45f-345f-4b84-8309-aea96684989c-container.json     (0.4 KB, 2026-03-25)
│   ├── 0f89b1b3-45c6-4a30-92ec-a0ff770f95cb-result.json        (7.6 KB, 2026-03-25)
│   ├── 1349ed5c-eb06-481a-8a9a-f931256369b5-container.json     (0.2 KB, 2026-03-25)
│   ├── 14220ab7-f5b6-43c1-91bb-fa1acb36bbc3-result.json        (7.6 KB, 2026-03-25)
│   ├── 146911c4-3d42-4448-bc48-7ba76e03c9cf-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 158411f4-3f6d-4539-8390-6c0d8a67d6bc-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 1734d9d8-e776-4b0b-95b2-3dbbfd786cc6-result.json        (7.6 KB, 2026-03-25)
│   ├── 1837fc3e-8575-4c3c-978b-1c5938c2b0cc-container.json     (0.2 KB, 2026-03-25)
│   ├── 186ce1a4-a4a5-4473-822c-eb0ebbfbfad6-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 19182218-1d2c-4a3b-b1ff-c4d1e5b59b96-container.json     (1.0 KB, 2026-03-25)
│   ├── 19d2b58e-2c31-48c7-a909-7936a1cf7284-container.json     (0.2 KB, 2026-03-25)
│   ├── 1a42012d-019f-4b33-9f06-8187a066091b-container.json     (0.4 KB, 2026-03-25)
│   ├── 1c4c455e-4681-4078-8c76-b3ff2e4a6161-container.json     (0.4 KB, 2026-03-25)
│   ├── 1cd51972-8c79-4500-a907-495c1e69ee75-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 1cd5d92f-8023-4088-a11f-9f1b4642de90-container.json     (0.4 KB, 2026-03-25)
│   ├── 1d0d0056-7f88-4559-8a5d-e07268950114-container.json     (0.4 KB, 2026-03-25)
│   ├── 1d665289-6a25-4e70-b74c-f7577959d89a-container.json     (0.4 KB, 2026-03-25)
│   ├── 1e152c89-fd16-4c68-885a-118ed57c33cc-container.json     (0.4 KB, 2026-03-25)
│   ├── 1e6b9c23-8027-42aa-9a03-9222c3345fa6-container.json     (0.2 KB, 2026-03-25)
│   ├── 221b099e-6d6d-4192-9043-cc24df4f980b-result.json        (7.6 KB, 2026-03-25)
│   ├── 22b5f355-86e8-467c-89ea-624cc6fba6f3-container.json     (1.0 KB, 2026-03-25)
│   ├── 234c90f2-96c5-4a64-ba90-462e780c7286-container.json     (0.2 KB, 2026-03-25)
│   ├── 274a5486-65c8-4798-b1c8-2cbb858fc67b-container.json     (0.2 KB, 2026-03-25)
│   ├── 2772bbc7-5f34-4e11-bded-1f8e6089f58f-container.json     (0.2 KB, 2026-03-25)
│   ├── 2a8960f4-1374-49a8-9c89-6e660331e078-container.json     (0.4 KB, 2026-03-25)
│   ├── 2b7df965-2b9e-4f66-9d1b-6b0e7c5e904c-container.json     (0.2 KB, 2026-03-25)
│   ├── 2c575379-0f18-42e0-a63b-10b33159b6f6-container.json     (0.2 KB, 2026-03-25)
│   ├── 2c712994-8217-42d1-b985-877f92773525-container.json     (1.0 KB, 2026-03-25)
│   ├── 3118ce96-3dad-4844-83f7-e3116ec09e74-container.json     (0.2 KB, 2026-03-25)
│   ├── 318135c7-c519-417f-939a-380ff80cae25-container.json     (1.0 KB, 2026-03-25)
│   ├── 31a610ff-2be7-492e-a8df-e4132d91d338-container.json     (0.2 KB, 2026-03-25)
│   ├── 33d893cf-66c0-4b99-87de-99826e89dc17-container.json     (0.2 KB, 2026-03-25)
│   ├── 34eb5474-349c-4e11-812b-63a1e033ac3a-result.json        (7.6 KB, 2026-03-25)
│   ├── 382e12a8-df97-468e-abe3-75309a08a331-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 38a2244e-6e66-4655-816c-b273b9afe799-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 38dc478d-2a83-420a-8141-d781a48fcc42-container.json     (0.2 KB, 2026-03-25)
│   ├── 3bc69984-6aea-45eb-8f48-0187d57e48a9-container.json     (0.2 KB, 2026-03-25)
│   ├── 3d5c4c08-64fa-4f7a-948e-99735e890117-container.json     (0.2 KB, 2026-03-25)
│   ├── 3e4c59ed-f49a-4525-bc94-ef39243015ee-container.json     (0.2 KB, 2026-03-25)
│   ├── 3e64c5e2-0462-4560-b83a-ea5dff8de443-container.json     (0.2 KB, 2026-03-25)
│   ├── 3ed057be-1d0d-4c65-a671-e638d3cd26fe-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 4159b655-864d-4f3f-a76b-dea9893d4385-container.json     (0.4 KB, 2026-03-25)
│   ├── 433791dd-4310-48c8-ac27-725dcebe7d12-container.json     (0.4 KB, 2026-03-25)
│   ├── 4490de44-3a63-4e5c-8212-caa539c13f33-container.json     (0.2 KB, 2026-03-25)
│   ├── 44b1f444-977c-4abd-ae2f-0b98ce772428-container.json     (0.2 KB, 2026-03-25)
│   ├── 44f73bbf-da01-4ec2-bba0-77db8f8dc8cb-container.json     (0.2 KB, 2026-03-25)
│   ├── 468e8cad-beb5-4adc-85b7-bb65844318db-container.json     (0.4 KB, 2026-03-25)
│   ├── 4875d014-4cc9-4c36-abb9-57bb7b48f694-container.json     (0.4 KB, 2026-03-25)
│   ├── 4bcc28a5-766c-41af-a6c1-15214b3c7c05-container.json     (0.2 KB, 2026-03-25)
│   ├── 4bcd6fc4-db1a-4db7-9903-ca100222c7de-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 4c0f3e76-532b-4a76-8e29-6dedab4c6b57-container.json     (1.1 KB, 2026-03-25)
│   ├── 4d143356-e0b1-448a-b17d-0222f63585c1-container.json     (0.2 KB, 2026-03-25)
│   ├── 4f5d12ad-e4ba-46fe-83f6-07ecbbbdd9d1-container.json     (0.2 KB, 2026-03-25)
│   ├── 4fad618e-887d-4cd7-a830-a3f33ffdca13-result.json        (7.6 KB, 2026-03-25)
│   ├── 50751ff0-b910-4561-8dab-6c971bda79ad-container.json     (0.2 KB, 2026-03-25)
│   ├── 5237f828-07d1-4bed-893b-c9798a31974d-container.json     (0.2 KB, 2026-03-25)
│   ├── 5386fa18-1c65-44d5-a388-cadcda48f941-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 53f6de56-ef4f-44b5-9acb-9a3719dca4d6-container.json     (0.2 KB, 2026-03-25)
│   ├── 54ccc37c-12a6-490d-b7f4-0854a34d7b98-result.json        (7.6 KB, 2026-03-25)
│   ├── 559b4eec-95ce-410e-a16a-43e92b801b49-result.json        (7.6 KB, 2026-03-25)
│   ├── 57c31312-5d9e-4923-bc92-f465248880fb-container.json     (0.2 KB, 2026-03-25)
│   ├── 5853f1ad-8d2f-4497-81f9-a31ea526ccfd-container.json     (0.2 KB, 2026-03-25)
│   ├── 593e3e7d-8ce8-4a1d-9751-4c1e91a311e9-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 59a38d8b-6658-46f1-9d33-d02240ce97f7-container.json     (0.2 KB, 2026-03-25)
│   ├── 5a5b0bc0-8c03-420b-b4da-c3b630541d19-container.json     (0.2 KB, 2026-03-25)
│   ├── 5b49d986-01fb-43e0-84b3-4ca6c2875b00-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 5c3a0514-948b-4d1e-b292-235c754809db-container.json     (0.2 KB, 2026-03-25)
│   ├── 5c7e3ddb-c07d-46ae-ab8e-95694636202c-container.json     (0.2 KB, 2026-03-25)
│   ├── 5c923859-4529-4f8d-8644-aa72d74a7f02-container.json     (0.4 KB, 2026-03-25)
│   ├── 6130184f-7468-4877-9b1c-bc5d8c05054a-container.json     (0.2 KB, 2026-03-25)
│   ├── 62207db2-5dcb-4aee-a77e-6b695c25313d-container.json     (0.2 KB, 2026-03-25)
│   ├── 62a69653-1ae3-42bc-8ac4-9c4d1387df82-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 6373b0b1-7226-414e-b227-c08ebb0c7969-container.json     (0.4 KB, 2026-03-25)
│   ├── 646eee9a-9d90-4079-908c-83c8d45d185a-container.json     (0.2 KB, 2026-03-25)
│   ├── 6530b430-3a0f-49a6-8701-75442fe42641-container.json     (1.0 KB, 2026-03-25)
│   ├── 66a46ce6-3e50-43d3-b26b-79ae2221ec4d-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 678389ff-729b-44bc-a79f-f8944bf77a88-container.json     (0.2 KB, 2026-03-25)
│   ├── 678e8592-8275-41de-b90b-166e323a3a4b-container.json     (0.4 KB, 2026-03-25)
│   ├── 67d709b6-1448-4231-901b-1691f8af1943-container.json     (0.4 KB, 2026-03-25)
│   ├── 68a1fcdb-9608-4c7a-b49d-e60273e0cfbc-container.json     (1.0 KB, 2026-03-25)
│   ├── 69dd0597-0858-4e2a-a7cf-e67533834796-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 6afcab27-604c-4449-bc83-fde43d4e61db-result.json        (7.6 KB, 2026-03-25)
│   ├── 6f162b7e-3dba-40bc-82be-6b7370110a59-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 710f2e2d-13dc-4214-ba8d-3d3944aed2ed-result.json        (7.6 KB, 2026-03-25)
│   ├── 72a84836-9baf-4eba-811b-ca7bf470c14c-container.json     (0.2 KB, 2026-03-25)
│   ├── 72d8b0a8-dcc9-474b-b908-917cdff15987-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 73661193-ecf4-4494-80c8-a35b611b0901-result.json        (7.6 KB, 2026-03-25)
│   ├── 7526e198-576b-4a2a-8549-872bfc8ae118-container.json     (0.2 KB, 2026-03-25)
│   ├── 75a77193-483f-4502-ae34-89db041502a9-container.json     (0.2 KB, 2026-03-25)
│   ├── 75d752bd-13f1-4e56-8156-5b3b45682207-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 77c3bd33-7f30-4729-a8ba-2e791492e515-result.json        (7.6 KB, 2026-03-25)
│   ├── 781d1f9c-7f7c-46b4-9e97-20b97b3a6658-result.json        (7.6 KB, 2026-03-25)
│   ├── 7840a079-e3e2-48bb-bb32-da880e8c735c-result.json        (7.6 KB, 2026-03-25)
│   ├── 78ce4743-4c1f-4c08-b5de-6cddc7113d9a-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 79455520-3a89-4af3-a0d2-53b80afbacd0-container.json     (0.4 KB, 2026-03-25)
│   ├── 7984ac24-0c1e-4bd6-95a3-cb9700d1b8b9-container.json     (0.2 KB, 2026-03-25)
│   ├── 7c63d59f-1e4e-4a40-993e-da19d1052762-container.json     (0.2 KB, 2026-03-25)
│   ├── 7de728c6-7836-40ec-9b10-eee5a6e14d32-container.json     (0.4 KB, 2026-03-25)
│   ├── 829c8b04-a598-4f20-8b7b-e9daf131b0e7-container.json     (0.4 KB, 2026-03-25)
│   ├── 854cacd2-d71a-4311-9656-cf59d6091ede-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── 8654988f-0022-4abe-a2f9-7da53dce3f47-container.json     (1.2 KB, 2026-03-25)
│   ├── 87c1fd1b-892e-4fa1-aa56-71497bbae390-container.json     (0.2 KB, 2026-03-25)
│   ├── 87d6b10e-c8b3-4c8a-bb7c-a5d961b20635-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 89a975a1-6b7a-408b-9fb5-7a64f0319495-container.json     (0.2 KB, 2026-03-25)
│   ├── 89eb6370-e1c0-425c-a42f-ef9bdc5c756f-container.json     (0.2 KB, 2026-03-25)
│   ├── 8a93ca37-9d40-4c44-a887-4d3e011843da-container.json     (0.4 KB, 2026-03-25)
│   ├── 8e981ac8-1fdb-4a0e-9874-f55837d844b7-container.json     (0.2 KB, 2026-03-25)
│   ├── 90215cbb-e9f9-49a8-9bdb-50e93b2bc81c-container.json     (0.2 KB, 2026-03-25)
│   ├── 913faf97-1e21-433a-89dc-df74c4c7c43d-container.json     (0.2 KB, 2026-03-25)
│   ├── 977f92f9-b589-4e07-a972-a7787e2a660c-container.json     (0.2 KB, 2026-03-25)
│   ├── 98aa508e-e921-433c-8f8c-f2d9f146af83-container.json     (0.4 KB, 2026-03-25)
│   ├── 9a1e9ef7-4ed2-4aa8-93fc-a2f999f422ca-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 9aacf52b-42e2-4152-a26a-d38a66950269-container.json     (0.4 KB, 2026-03-25)
│   ├── 9aada197-2566-4b21-bc94-4c66dfcfb960-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 9bb5e957-bbc1-4ee4-89f2-4a57bee08197-container.json     (1.1 KB, 2026-03-25)
│   ├── 9d09a2c0-1b0f-423c-8779-e1e9a8fcf642-container.json     (0.2 KB, 2026-03-25)
│   ├── 9e118abe-d1ea-4ecf-8ee8-88970d5a7f98-container.json     (0.2 KB, 2026-03-25)
│   ├── 9ee39e90-362b-440b-8d48-81b18437bf7b-container.json     (0.2 KB, 2026-03-25)
│   ├── 9f257e2e-ab7b-4d4d-936d-5126a1f4d0a3-container.json     (0.2 KB, 2026-03-25)
│   ├── a072de5f-8ac6-4ab0-a06f-132d3f63d1c6-container.json     (0.2 KB, 2026-03-25)
│   ├── a22b4990-e96e-49b0-84b0-dc40c1a51fa4-attachment.txt     (0.0 KB, 2026-03-25)
│   ├── a3a4f43d-97a9-404b-a7d0-63a9870274b5-container.json     (0.2 KB, 2026-03-25)
│   ├── a6403d66-477e-4649-9a3f-7d0af96cd4f9-container.json     (0.2 KB, 2026-03-25)
│   ├── a787d48e-f621-496d-af23-3d1a48582dbc-container.json     (0.2 KB, 2026-03-25)
│   ├── a957efb7-96b0-4b06-9eb3-f0da57eb1a3f-container.json     (0.4 KB, 2026-03-25)
│   ├── aa00e0b2-45d6-4040-85bd-74a58079bf8f-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── ab7f7d2e-5690-4f18-98c1-2f777f799a07-container.json     (0.4 KB, 2026-03-25)
│   ├── abb9c4fd-067f-4993-9e79-99887e014414-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── ac013d3e-3daf-41f7-8834-4489cf5458f5-container.json     (0.2 KB, 2026-03-25)
│   ├── b0cb6a36-b32a-45f0-828b-4d370decc459-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── b1131783-441a-45e8-9200-8aef215267d0-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── b2dd6628-f12e-4d9a-a17a-675ee588aa36-container.json     (0.4 KB, 2026-03-25)
│   ├── b447477f-7bca-4bcd-8f3e-4670b074a039-container.json     (0.2 KB, 2026-03-25)
│   ├── b5b265f5-7f8a-488e-80b7-3e9d6d8a9108-container.json     (0.2 KB, 2026-03-25)
│   ├── b6d73eff-cd0e-49d1-968e-8c2f4c759989-container.json     (0.2 KB, 2026-03-25)
│   ├── b75dfbc9-5779-4f24-801a-e51b0b04fa16-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── b7f2a907-fede-4599-bccd-52abc070a7d0-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── b834217c-2010-4f96-a485-a1d083f17013-container.json     (0.2 KB, 2026-03-25)
│   ├── bdcdc730-8259-473a-ad20-d13e1194078f-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── bf2e3069-5f43-420c-98e8-a68a12f94bba-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── bffcfbb1-cbd4-4708-b2a6-f9a302304750-container.json     (1.0 KB, 2026-03-25)
│   ├── c3741030-df06-47e4-be7b-34ca38997c0a-container.json     (0.2 KB, 2026-03-25)
│   ├── c47bfb15-c3ab-4e2a-a41e-06346e8d822d-container.json     (0.4 KB, 2026-03-25)
│   ├── c5530ab9-8cad-4f01-a9c9-32ab17a7ff67-result.json        (7.6 KB, 2026-03-25)
│   ├── c57e9b73-f7cb-42ee-acd9-eb418bc21674-container.json     (0.2 KB, 2026-03-25)
│   ├── c6cbc383-743e-46e0-bd54-2b1cc105a44f-container.json     (0.4 KB, 2026-03-25)
│   ├── c8f33508-dd76-4751-b1a1-cb1b7db46168-container.json     (0.4 KB, 2026-03-25)
│   ├── ca35ba48-4fa2-47d6-a236-7bf4a12dd56e-container.json     (0.2 KB, 2026-03-25)
│   ├── cacb1f52-5b5e-425d-b9fc-55c85dc5442f-container.json     (0.2 KB, 2026-03-25)
│   ├── cb7e8034-d828-4f6d-96d5-05bf484754cb-container.json     (0.4 KB, 2026-03-25)
│   ├── cc8c8ea9-40a2-46d8-add3-ef018ace2c27-container.json     (0.4 KB, 2026-03-25)
│   ├── cf5b5f26-ac62-4b43-9468-9b4335c42521-result.json        (7.6 KB, 2026-03-25)
│   ├── d0c29ae5-2487-4e17-92bf-dfd5bebc91d3-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── d2c97e48-5cd2-46e4-a33c-01b721bc09e6-container.json     (0.2 KB, 2026-03-25)
│   ├── d337bd35-a27b-4637-ae5e-b3e572a2b293-container.json     (0.4 KB, 2026-03-25)
│   ├── d4ba4067-e57d-40d6-a592-dc2d3fcc3d53-container.json     (0.4 KB, 2026-03-25)
│   ├── d573e0fc-c338-44aa-ad61-a27a26e8ec3c-container.json     (0.2 KB, 2026-03-25)
│   ├── d6947c1f-14b6-4939-b664-bc41e6ea77e6-result.json        (7.6 KB, 2026-03-25)
│   ├── d6a79a3f-c426-4e50-bf3d-22d96455bf56-container.json     (0.2 KB, 2026-03-25)
│   ├── d8bd4ba5-1292-4adc-9218-18ea8bb05fab-container.json     (1.1 KB, 2026-03-25)
│   ├── dd75ced4-9068-4b97-9646-7389906910d1-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── ddbb225c-6ef3-4853-b48e-5bfe632c4281-container.json     (0.4 KB, 2026-03-25)
│   ├── ddf2d10c-48ef-4128-b757-2a911410d25e-container.json     (0.2 KB, 2026-03-25)
│   ├── de033b7a-d8f1-455d-b419-153cb7323cb2-container.json     (0.2 KB, 2026-03-25)
│   ├── debf7b57-6535-447d-9984-e104cfa0599a-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── e11d9916-e274-4b70-9c07-06e9594d5e3e-container.json     (0.2 KB, 2026-03-25)
│   ├── e59075d1-2800-47d2-afd2-be5ff4e0ea0e-container.json     (0.2 KB, 2026-03-25)
│   ├── e703569d-5462-4ca2-9924-8efd340747c9-result.json        (7.6 KB, 2026-03-25)
│   ├── e717484c-4df0-44cc-9ce3-580daba3c75a-container.json     (0.4 KB, 2026-03-25)
│   ├── e7bfa04e-b41d-4be8-b8f1-1319ec694faf-container.json     (0.2 KB, 2026-03-25)
│   ├── e94f31e6-b657-4391-a090-aca8b50d6f2c-container.json     (0.2 KB, 2026-03-25)
│   ├── e97c1b51-45ea-4ebf-b8b6-4327742cef97-container.json     (0.4 KB, 2026-03-25)
│   ├── eec53211-1892-480a-96c0-72da057d4938-container.json     (0.2 KB, 2026-03-25)
│   ├── f0217a30-deda-4e4c-9a30-9a9bce05c9c2-container.json     (0.2 KB, 2026-03-25)
│   ├── f027de4e-e666-4727-9743-7b2f2477988e-container.json     (1.0 KB, 2026-03-25)
│   ├── f03dfd4a-37f2-4b5f-8b8d-b35ae0c3c5c3-container.json     (0.4 KB, 2026-03-25)
│   ├── f1f5a584-3c8e-4e4c-8b21-90208e557043-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── f1fa1fca-6a43-4931-b791-1cd243cdddf0-container.json     (0.4 KB, 2026-03-25)
│   ├── f33c8847-9c78-41cf-a2dc-f3a50915cee3-container.json     (0.2 KB, 2026-03-25)
│   ├── f38c8b74-8b94-4839-9ae9-d72adf29a17d-result.json        (7.6 KB, 2026-03-25)
│   ├── f5c33732-f8cd-4af6-b615-ba65497b6c86-result.json        (7.6 KB, 2026-03-25)
│   ├── f5cf2377-e7b5-4f0c-9710-e4c23894d9d5-container.json     (0.2 KB, 2026-03-25)
│   ├── f6dc8745-1f08-4bea-bf3f-def127ac6a32-container.json     (0.2 KB, 2026-03-25)
│   ├── f7116a6d-84a2-43ca-8504-baac5904a11a-container.json     (0.4 KB, 2026-03-25)
│   ├── f7d31cf6-5867-4bcf-85af-1045a0135d86-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── fa6220fa-b94b-42bf-a914-bfd100c1db5a-container.json     (1.0 KB, 2026-03-25)
│   ├── fbbc1243-acee-4745-b871-76256ec297a2-attachment.attach  (0.0 KB, 2026-03-25)
│   └── fbd42c01-6132-4d34-93b0-189020c9175c-container.json     (1.0 KB, 2026-03-25)
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
│   ├── QA_Integration_Report_20260325_024102.xlsx  (7.4 KB, 2026-03-25)
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