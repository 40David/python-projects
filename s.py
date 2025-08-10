from docx import Document

# Load the previously saved document
doc = Document("/Users/vishwass/Downloads")

# Replace the references with APA-style citations
new_references = [
    "Zhao, R., Yan, R., Chen, Z., Mao, K., Wang, P., & Gao, R. X. (2020). Deep learning and its applications to machine health monitoring. *Mechanical Systems and Signal Processing, 115*, 213–237. https://doi.org/10.1016/j.ymssp.2018.05.050",
    "Jardine, A. K. S., Lin, D., & Banjevic, D. (2006). A review on machinery diagnostics and prognostics implementing condition-based maintenance. *Mechanical Systems and Signal Processing, 20*(7), 1483–1510. https://doi.org/10.1016/j.ymssp.2005.09.012",
    "Susto, G. A., Schirru, A., Pampuri, S., McLoone, S., & Beghi, A. (2015). Machine learning for predictive maintenance: A multiple classifier approach. *IEEE Transactions on Industrial Informatics, 11*(3), 812–820. https://doi.org/10.1109/TII.2014.2349359"
]

# Find and replace the old references section
for para in doc.paragraphs:
    if para.text.strip().startswith("Zhao, R."):
        para.text = new_references[0]
    elif para.text.strip().startswith("Jardine, A."):
        para.text = new_references[1]
    elif para.text.strip().startswith("Susto, G."):
        para.text = new_references[2]

# Save updated document
updated_path = "/Users/vishwass/Downloads/Predictive_Maintenance_Synopsis_APA.docx"
doc.save(updated_path)

updated_path