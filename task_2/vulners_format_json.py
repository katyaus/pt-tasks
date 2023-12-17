import json


def formatting_json_report(path: str):
    report_dict = None
    try:
        with open(path, "r", encoding="utf-8") as input_file:
            report_dict = json.load(input_file)
    except FileNotFoundError:
        print(f'Не удается получить доступ к файлу "{path}".')
        return

    source_alerts = report_dict['site'][0]['alerts']
    vulnerabilities = []

    for alert in source_alerts:
        vulnerabilities.append({'name':alert['name'].strip(), 'count':int(alert['count'])})

    changed_report = {'vulnerabilities':vulnerabilities}

    with open('upd_report.json', 'w', encoding='utf-8') as output_file:
        json.dump(changed_report, output_file, indent=4, ensure_ascii=False)

formatting_json_report("ZAP-report_example.json")