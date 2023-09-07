# -*- coding: utf-8 -*-
"""CSV to PDF_Using _Python_Task To Analytics .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXJyZmqRyCVWzmPbWmc3Uib1GB8kTRVz
"""

import pandas as pd

bookings_df = pd.read_csv('/content/bookings.csv')

bookings_df.head(23)

bookings_df_filled = bookings_df.fillna('N/A')

bookings_df_cleaned = bookings_df_filled.drop(columns=bookings_df_filled.columns[bookings_df_filled.eq("N/A").all()])

bookings_df_cleaned.head(23)

import numpy as np

random_amounts = np.random.choice(range(600, 4001, 100), size=bookings_df_cleaned.shape[0])

bookings_df_cleaned['amount'] = random_amounts

bookings_df_cleaned.head(23)

!pip install fpdf

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Ground Bookings Data', 0, 1, 'C')

def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def df_to_pdf(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    col_width = pdf.get_string_width(max(dataframe.columns, key=lambda x: len(x))) + 6  # padding
    row_height = 10

    # Print header
    for col in dataframe.columns:
        pdf.cell(col_width, row_height, col, border=1)
    pdf.ln(row_height)

    # Print rows
    for _, row in dataframe.iterrows():
        for item in row:
            pdf.cell(col_width, row_height, str(item), border=1)
        pdf.ln(row_height)

    return pdf

# Convert DataFrame to PDF
pdf_path = "bookings_updated_further_reduced.pdf"
pdf = df_to_pdf(bookings_df_cleaned)
pdf.output(pdf_path)

pdf_path

# Remove the specified columns from the DataFrame
columns_to_remove = [
    "contact_name", "is_cancel", "contact_number", "updated_at", "created_at",
    "payment_signature", "payment_pgTxnNo", "app_name", "id", "user_id", "ground_id"
]
bookings_df_reduced = bookings_df_cleaned.drop(columns=columns_to_remove)

# Adjust the PDF generation function to reduce font size and layout in landscape mode
class PDF(FPDF):
    def __init__(self, orientation='L'):
        super().__init__(orientation=orientation)

    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, 'Ground Bookings Data', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def df_to_pdf(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    col_width = pdf.get_string_width(max(dataframe.columns, key=lambda x: len(x))) + 6  # padding
    row_height = 8
    pdf.set_font_size(8)

    # Print header
    for col in dataframe.columns:
        pdf.cell(col_width, row_height, col, border=1)
    pdf.ln(row_height)

    # Print rows
    for _, row in dataframe.iterrows():
        for item in row:
            pdf.cell(col_width, row_height, str(item), border=1)
        pdf.ln(row_height)

    return pdf

# Convert the reduced DataFrame to PDF
pdf_path_reduced = "bookings_updated_further_reduced.pdf"
pdf = df_to_pdf(bookings_df_reduced)
pdf.output(pdf_path_reduced)

pdf_path_reduced

# Define the list of additional columns to remove
additional_columns_to_remove = ['column_name1', 'column_name2', 'column_name3']

# Remove valid columns from the DataFrame
valid_columns_to_remove = [col for col in additional_columns_to_remove if col in bookings_df_reduced.columns]
bookings_df_further_reduced = bookings_df_reduced.drop(columns=valid_columns_to_remove)

# Convert the further reduced DataFrame to PDF again
pdf_path_further_reduced = "bookings_updated_further_reduced.pdf"
pdf = df_to_pdf(bookings_df_further_reduced)
pdf.output(pdf_path_further_reduced)

pdf_path_further_reduced

# Remove valid columns from the DataFrame
valid_columns_to_remove = [col for col in additional_columns_to_remove if col in bookings_df_reduced.columns]
bookings_df_further_reduced = bookings_df_reduced.drop(columns=valid_columns_to_remove)

# Convert the further reduced DataFrame to PDF
pdf_path_further_reduced = "bookings_updated_further_reduced.pdf"  # Specify the output PDF file path
pdf = df_to_pdf(bookings_df_further_reduced)
pdf.output(pdf_path_further_reduced)

print(f'PDF file "{pdf_path_further_reduced}" has been created successfully.')

# Remove the newly specified columns from the DataFrame
new_columns_to_remove = ["payment_issuerRefNo", "timing_id"]
bookings_df_final = bookings_df_further_reduced.drop(columns=new_columns_to_remove)

# Convert the final DataFrame to PDF
pdf_path_final = "/bookings_final.pdf"
pdf = df_to_pdf(bookings_df_final)
pdf.output(pdf_path_final)

pdf_path_final

# Remove the newly specified columns from the DataFrame
new_columns_to_remove = ["payment_issuerRefNo", "timing_id"]
bookings_df_final = bookings_df_further_reduced.drop(columns=new_columns_to_remove)

# Convert the final DataFrame to PDF
pdf_path_final = "/content/bookings_updated_further_reduced.pdf"  # Specify the output PDF file path
pdf = df_to_pdf(bookings_df_final)
pdf.output(pdf_path_final)

# Access the final PDF file path
print(f'PDF file "{pdf_path_final}" has been created successfully.')

# You can now access the generated PDF at pdf_path_final

def df_to_pdf_adjusted(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Set custom width for the "ground_name" column
    ground_name_width = pdf.get_string_width(max(dataframe["ground_name"], key=lambda x: len(x))) + 6
    default_col_width = pdf.get_string_width(max(dataframe.columns, key=lambda x: len(x))) + 6  # padding
    row_height = 8
    pdf.set_font_size(8)

    # Print header
    for col in dataframe.columns:
        if col == "ground_name":
            pdf.cell(ground_name_width, row_height, col, border=1)
        else:
            pdf.cell(default_col_width, row_height, col, border=1)
    pdf.ln(row_height)

    # Print rows
    for _, row in dataframe.iterrows():
        for col, item in zip(dataframe.columns, row):
            if col == "ground_name":
                pdf.cell(ground_name_width, row_height, str(item), border=1)
            else:
                pdf.cell(default_col_width, row_height, str(item), border=1)
        pdf.ln(row_height)

    return pdf

# Convert the final DataFrame to PDF with adjusted column width
pdf_path_adjusted = "/content/bookings_updated_further_reduced.pdf"
pdf = df_to_pdf_adjusted(bookings_df_final)
pdf.output(pdf_path_adjusted)

pdf_path_adjusted

def df_to_pdf_final(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Set custom width for the "ground_name" and "username" columns
    ground_name_width = pdf.get_string_width(max(dataframe["ground_name"], key=lambda x: len(x))) + 6
    username_width = pdf.get_string_width(max(dataframe["username"], key=lambda x: len(x))) + 6
    default_col_width = pdf.get_string_width(max(dataframe.columns, key=lambda x: len(x))) + 6  # padding
    row_height = 8
    pdf.set_font_size(8)

    # Print header
    for col in dataframe.columns:
        if col == "ground_name":
            pdf.cell(ground_name_width, row_height, col, border=1)
        elif col == "username":
            pdf.cell(username_width, row_height, col, border=1)
        else:
            pdf.cell(default_col_width, row_height, col, border=1)
    pdf.ln(row_height)

    # Print rows
    for _, row in dataframe.iterrows():
        for col, item in zip(dataframe.columns, row):
            if col == "ground_name":
                pdf.cell(ground_name_width, row_height, str(item), border=1)
            elif col == "username":
                pdf.cell(username_width, row_height, str(item), border=1)
            else:
                pdf.cell(default_col_width, row_height, str(item), border=1)
        pdf.ln(row_height)

    # Add summary data on the last page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Summary Data', 0, 1, 'C')

    # Total unique booking by ground_name and their total amount
    summary_data = dataframe.groupby("ground_name").agg(
        total_bookings=pd.NamedAgg(column="amount", aggfunc="count"),
        total_amount=pd.NamedAgg(column="amount", aggfunc="sum")
    ).reset_index()

    pdf.set_font_size(10)
    pdf.ln(10)
    for _, row in summary_data.iterrows():
        pdf.cell(0, 10, f"Ground Name: {row['ground_name']}", ln=True)
        pdf.cell(0, 10, f"Total Bookings: {row['total_bookings']}", ln=True)
        pdf.cell(0, 10, f"Total Amount: {row['total_amount']}", ln=True)
        pdf.ln(10)

    # Total amount
    total_amount = dataframe["amount"].sum()
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Overall Total Amount: {total_amount}", 0, 1, 'C')

    return pdf

# Convert the final DataFrame to PDF with adjusted column width and summary data
pdf_path_final = "/content/bookings_updated_further_reduced.pdf"
pdf = df_to_pdf_final(bookings_df_final)
pdf.output(pdf_path_final)

pdf_path_final

def df_to_pdf_with_table_summary(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Set custom width for the "ground_name" and "username" columns
    ground_name_width = pdf.get_string_width(max(dataframe["ground_name"], key=lambda x: len(x))) + 6
    username_width = pdf.get_string_width(max(dataframe["username"], key=lambda x: len(x))) + 6
    default_col_width = pdf.get_string_width(max(dataframe.columns, key=lambda x: len(x))) + 6  # padding
    row_height = 8
    pdf.set_font_size(8)

    # Print header
    for col in dataframe.columns:
        if col == "ground_name":
            pdf.cell(ground_name_width, row_height, col, border=1)
        elif col == "username":
            pdf.cell(username_width, row_height, col, border=1)
        else:
            pdf.cell(default_col_width, row_height, col, border=1)
    pdf.ln(row_height)

    # Print rows
    for _, row in dataframe.iterrows():
        for col, item in zip(dataframe.columns, row):
            if col == "ground_name":
                pdf.cell(ground_name_width, row_height, str(item), border=1)
            elif col == "username":
                pdf.cell(username_width, row_height, str(item), border=1)
            else:
                pdf.cell(default_col_width, row_height, str(item), border=1)
        pdf.ln(row_height)

    # Add summary data on the last page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Summary Data', 0, 1, 'C')

    # Total unique booking by ground_name and their total amount
    summary_data = dataframe.groupby("ground_name").agg(
        total_bookings=pd.NamedAgg(column="amount", aggfunc="count"),
        total_amount=pd.NamedAgg(column="amount", aggfunc="sum")
    ).reset_index()

    pdf.set_font_size(10)
    pdf.ln(10)

    # Print header for summary table
    summary_headers = ["Ground Name", "Total Bookings", "Total Amount"]
    summary_col_widths = [
        pdf.get_string_width(max(summary_data["ground_name"], key=lambda x: len(x))) + 6,
        pdf.get_string_width(str(max(summary_data["total_bookings"]))) + 6,
        pdf.get_string_width(str(max(summary_data["total_amount"]))) + 6
    ]
    for header, col_width in zip(summary_headers, summary_col_widths):
        pdf.cell(col_width, row_height, header, border=1)
    pdf.ln(row_height)

    # Print rows for summary table
    for _, row in summary_data.iterrows():
        pdf.cell(summary_col_widths[0], row_height, str(row['ground_name']), border=1)
        pdf.cell(summary_col_widths[1], row_height, str(row['total_bookings']), border=1)
        pdf.cell(summary_col_widths[2], row_height, str(row['total_amount']), border=1)
        pdf.ln(row_height)

    # Total amount
    total_amount = dataframe["amount"].sum()
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Overall Total Amount: {total_amount}", 0, 1, 'C')

    return pdf

# Convert the final DataFrame to PDF with adjusted column width and tabular summary data
pdf_path_table_summary = "/content/bookings_table_fixed_summary.pdf"
pdf = df_to_pdf_with_table_summary(bookings_df_final)
pdf.output(pdf_path_table_summary)

pdf_path_table_summary

def df_to_pdf_with_fixed_table_summary(dataframe):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Set custom width for the "ground_name" and "username" columns
    ground_name_width = pdf.get_string_width(max(dataframe["ground_name"], key=lambda x: len(x))) + 6
    username_width = pdf.get_string_width(max(dataframe["username"], key=lambda x: len(x))) + 6
    default_col_width = pdf.get_string_width(max(dataframe.columns, key=lambda x: len(x))) + 6  # padding
    row_height = 8
    pdf.set_font_size(8)

    # Print header
    for col in dataframe.columns:
        if col == "ground_name":
            pdf.cell(ground_name_width, row_height, col, border=1)
        elif col == "username":
            pdf.cell(username_width, row_height, col, border=1)
        else:
            pdf.cell(default_col_width, row_height, col, border=1)
    pdf.ln(row_height)

    # Print rows
    for _, row in dataframe.iterrows():
        for col, item in zip(dataframe.columns, row):
            if col == "ground_name":
                pdf.cell(ground_name_width, row_height, str(item), border=1)
            elif col == "username":
                pdf.cell(username_width, row_height, str(item), border=1)
            else:
                pdf.cell(default_col_width, row_height, str(item), border=1)
        pdf.ln(row_height)

    # Add summary data on the last page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Summary Data', 0, 1, 'C')

    # Total unique booking by ground_name and their total amount
    summary_data = dataframe.groupby("ground_name").agg(
        total_bookings=pd.NamedAgg(column="amount", aggfunc="count"),
        total_amount=pd.NamedAgg(column="amount", aggfunc="sum")
    ).reset_index()

    pdf.set_font_size(10)
    pdf.ln(10)

    # Print header for summary table
    summary_headers = ["Ground Name", "Total Bookings", "Total Amount (INR)"]
    summary_col_widths = [
        pdf.get_string_width(max(summary_data["ground_name"], key=lambda x: len(x))) + 6,
        pdf.get_string_width("Total Bookings") + 6,
        pdf.get_string_width("Total Amount (INR)") + 6
    ]
    for header, col_width in zip(summary_headers, summary_col_widths):
        pdf.cell(col_width, row_height, header, border=1)
    pdf.ln(row_height)

    # Print rows for summary table
    for _, row in summary_data.iterrows():
        pdf.cell(summary_col_widths[0], row_height, str(row['ground_name']), border=1)
        pdf.cell(summary_col_widths[1], row_height, str(row['total_bookings']), border=1)
        pdf.cell(summary_col_widths[2], row_height, f"INR {row['total_amount']}", border=1)
        pdf.ln(row_height)

    # Total amount
    total_amount = dataframe["amount"].sum()
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Overall Total Amount: INR {total_amount}", 0, 1, 'C')

    return pdf

# Convert the final DataFrame to PDF with fixed tabular summary data
pdf_path_table_fixed_summary = "/content/bookings_table_fixed_summary.pdf"
pdf = df_to_pdf_with_fixed_table_summary(bookings_df_final)
pdf.output(pdf_path_table_fixed_summary)

pdf_path_table_fixed_summary