/*
    Created from:
        Messages = {{globals.inputfilename}}
        Template = {{globals.templatefilename}}
        Language = {{globals.languagefilename}}

                     AUTOGENERATED FILE, DO NOT EDIT

*/
{% macro fieldType(field)  %}
    {%- if "int" in field.Type -%}
{{field.Type + "_t"}}
    {%- elif field.Type.lower() == "float32" -%}
float
    {%- elif field.Type.lower() == "float64" -%}
double
    {%- else -%}
?
    {%- endif -%}
{%- endmacro -%}
{{'#'}}ifndef {{globals.msgname}}Code_H__
{{'#'}}define {{globals.msgname}}Code_H__

{{'#'}}define {{globals.msgname}}_MSG_ID {{globals.msgid}}
{{'#'}}define {{globals.msgname}}_MSG_SIZE {{globals.msgsize}}
<ENUMERATIONS>

#for f in msg.Fields:
{{"#define "~globals.msgname~"_"~f.Name~"_DEFAULT "~f.Default~"\n" if f.Default is defined-}}
{{"#define "~globals.msgname~"_"~f.Name~"_COUNT "~f.Count~"\n" if f.Count is defined-}}
{{"#define "~globals.msgname~"_"~f.Name~"_OFFSET "~f.Location }}
{{"#define "~globals.msgname~"_"~f.Name~"_SIZE "~msgutils.fieldSize(f)}}
{%for bf in f.Bitfields%}
{{"#define "~globals.msgname~"_"~bf.Name~"_DEFAULT "~bf.Default~"\n" if bf.Default is defined -}}
{%endfor%}
#endfor


#for f in msg.Fields:
/*  {{f.Units}}, ({{msgutils.fieldMin(f)}} to {{msgutils.fieldMax(f)}})*/
INLINE {{fieldType(f)}} {{globals.msgname}}_Get{{f.Name}}(uint8_t* m_data{%if msgutils.fieldCount(f) > 1%}, int idx{%endif%})
{
    {% set access %}Get_{{fieldType(f)}}(&m_data[{{f.Location}}{%if msgutils.fieldCount(f) > 1%}+idx*{{msgutils.fieldSize(f)}}{%endif%}]){% endset %}
    return {{ msgutils.getMath(access, f, msgutils.typeForScaledInt(f), 'f') }};
}
    #for bf in f.Bitfields:
/*  {{bf.Units}}, ({{msgutils.fieldMin(bf)}} to {{msgutils.fieldMax(bf)}})*/
INLINE {{fieldType(f)}} {{globals.msgname}}_Get{{bf.Name}}(uint8_t* m_data)
{
    return ({{globals.msgname}}_Get{{f.Name}}(m_data) >> {{bf.BitLocation}}) & {{msgutils.Mask(bf.NumBits)}};
}
    #endfor
#endfor
#for f in msg.Fields:
/*  {{f.Units}}, ({{msgutils.fieldMin(f)}} to {{msgutils.fieldMax(f)}})*/
INLINE void {{globals.msgname}}_Set{{f.Name}}(uint8_t* m_data, {{fieldType(f)}} value{%if msgutils.fieldCount(f) > 1%}, int idx{%endif%})
{
    Set_{{fieldType(f)}}(&m_data[{{f.Location}}{%if msgutils.fieldCount(f) > 1%}+idx*{{msgutils.fieldSize(f)}}{%endif%}], value);
}
    #for bf in f.Bitfields:
/*  {{bf.Units}}, ({{msgutils.fieldMin(bf)}} to {{msgutils.fieldMax(bf)}})*/
INLINE void {{globals.msgname}}_Set{{bf.Name}}(uint8_t* m_data, {{fieldType(f)}} value)
{
    {{globals.msgname}}_Set{{f.Name}}(m_data, ({{globals.msgname}}_Get{{f.Name}}(m_data) & ~({{msgutils.Mask(bf.NumBits)}} << {{bf.BitLocation}})) | ((value & {{msgutils.Mask(bf.NumBits)}}) << {{bf.BitLocation}}));
}
    #endfor
#endfor
INLINE void {{globals.msgname}}_Init(uint8_t* m_data)
{
    # for f in msg.Fields:
        # if f.Default is defined:
            # if f.Count is defined and f.Count != 1:
    for (int i=0; i<{{f.Count}}; i++)
        {{globals.msgname}}_Set{{f.Name}}(m_data, {{f.Default}}, i);
            # else:
    {{globals.msgname}}_Set{{f.Name}}(m_data, {{f.Default}});
            # endif
        # endif
        # for bf in f.Bitfields:
            # if bf.Default is defined:
    {{globals.msgname}}_Set{{bf.Name}}(m_data, {{bf.Default}});
            #endif
        #endfor
    # endfor
}

{{'#'}}endif

