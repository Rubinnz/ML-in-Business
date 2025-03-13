import pandas as pd
import plotly.express as px

file_path = fr"D:\HK7\ML\ML-in-Business\nested_pie_chart_plot\dataset\dataset-416.xlsx"
xls = pd.ExcelFile(file_path)

df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

df_filtered = df.dropna(subset=['Tên học phần', 'Học Kỳ', 'Loại môn học'])

df_filtered = df_filtered.copy()
df_filtered['Học Kỳ'] = df_filtered['Học Kỳ'].astype(int).astype(str)

fig = px.sunburst(
    df_filtered,
    path=['Học Kỳ', 'Loại môn học', 'Tên học phần'],
    values=[1] * len(df_filtered),
    title="Biểu đồ Nested Pie Chart của các môn học theo kỳ",
    color='Loại môn học',
)

output_html = fr"D:\HK7\ML\ML-in-Business\nested_pie_chart_plot\416_10k.html"
fig.write_html(output_html)

print(f"Biểu đồ đã được lưu tại {output_html}. Hãy mở file này trong trình duyệt để xem.")
